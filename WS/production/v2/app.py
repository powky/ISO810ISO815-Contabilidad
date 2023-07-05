from flask import Flask, jsonify, request
from flask_cors import CORS
from config import config
from collections import OrderedDict
import cx_Oracle

app = Flask(__name__)
CORS(app)

# Inicializamos las variables de ambiente desde el archivo config.py
development_config = config["development"]
conn = development_config.conn
cursor = development_config.cursor

# API que devuelve todos los valores de la tabla sin filtrar
@app.route("/get-accounting-entries", methods=["GET"])
def listar_asientocontable():
    try:
        sql = "SELECT * FROM accounting_entries"
        cursor.execute(sql)
        datos = cursor.fetchall()
        print(datos)
        asientocontables = []
        for fila in datos:
            fecha_registro = fila[5].strftime("%Y-%m-%d")
            asientocontable = {
                "id": fila[0],
                "descripcion": fila[1],
                "auxiliar": fila[2],
                "cuentaContable": fila[3],
                "tipoMovimiento": fila[4],
                "fechaRegistro": fecha_registro,
                "monto": fila[6],
                "estado": fila[7],
            }
            asientocontables.append(asientocontable)
            asientocontables_ordered = [OrderedDict(item) for item in asientocontables]
        
        return jsonify(
            {
                "asientosContables": asientocontables_ordered,
                "mensaje": "Asiento contable listado.",
                "exito": True,
            }
        ), 200
    except Exception as ex:
        return jsonify({"mensaje": "Error al conectar o leer la DB", "exito": False}), 400

#------------------------------------------------------------------------------------------------------------------------
# API que devuelve los valores de la tabla por ID
#------------------------------------------------------------------------------------------------------------------------
@app.route("/get-accounting-entries/<codigo>", methods=["GET"])
def leer_asientocontable(codigo):
    try:
        asientocontable = leer_asientocontable_bd(codigo)
        if asientocontable is not None:
            return jsonify(
                {
                    "asientocontable": asientocontable,
                    "mensaje": "asiento contable listado.",
                    "exito": True,
                }
            ), 200
        else:
            return jsonify(
                {"mensaje": "No existe asiento contable con ese ID.", "exito": False}
            ), 500
    except Exception as ex:
        return jsonify({"mensaje": "Error interno.", "exito": False}), 400

# Funcion para filtrar dentro de la tabla usando ID
def leer_asientocontable_bd(codigo):
    try:
        sql = "SELECT * FROM accounting_entries WHERE id = '{0}'".format(
            codigo
        )
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            fecha_registro = datos[5].strftime("%Y-%m-%d")
            asientocontable = {
                "id": datos[0],
                "descripcion": datos[1],
                "auxiliar": datos[2],
                "cuentaContable": datos[3],
                "tipoMovimiento": datos[4],
                "fechaRegistro": fecha_registro,
                "monto": datos[6],
                "estado": datos[7],
            }
            return asientocontable
        else:
            return None
    except Exception as ex:
        raise ex
    
#------------------------------------------------------------------------------------------------------------------------
# API que devuelve los valores de la tabla por ID
#------------------------------------------------------------------------------------------------------------------------
@app.route("/get-accounting-entries/auxiliar=<id>", methods=["GET"])
def leer_asientocontable_aux(id):
    try:
        asientocontable = leer_asientocontable_bd_by_aux(id)
        if asientocontable is not None:
            return jsonify(
                {
                    "asientocontable": asientocontable,
                    "mensaje": "Asientos contables listados.",
                    "exito": True,
                }
            ), 200
        else:
            return jsonify(
                {"mensaje": "No existen asientos o el auxiliar no existe.", "exito": False}
            ), 500
    except Exception as ex:
        return jsonify({"mensaje": "Error interno.", "exito": False}), 400

# Funcion para filtrar dentro de la tabla usando ID de auxiliar 
def leer_asientocontable_bd_by_aux(id):
    try:
        sql = "SELECT * FROM accounting_entries WHERE aux_id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchall()
        asientos_contables = []  # Create an empty list to store multiple rows
        for row in datos:
            fecha_registro = row[5].strftime("%Y-%m-%d")
            asientocontable = {
                "id": row[0],
                "descripcion": row[1],
                "auxiliar": row[2],
                "cuentaContable": row[3],
                "tipoMovimiento": row[4],
                "fechaRegistro": fecha_registro,
                "monto": row[6],
                "estado": row[7],
            }
            asientos_contables.append(asientocontable)  # Append each row to the list
        return asientos_contables
    except Exception as ex:
        raise ex

#------------------------------------------------------------------------------------------------------------------------
# API de registrar cuentas contables
#------------------------------------------------------------------------------------------------------------------------
@app.route("/post-accounting-entries", methods=["POST"])
def registrar_asientocontable():
    try:
        data = request.json
        # Verifica que llegaron todos los valores en el request
        if (
            "descripcion" in data
            and "auxiliar" in data
            and "cuentaDB" in data
            and "cuentaCR" in data
            and "monto" in data
        ):
            # Asignamos los valores a variables
            i_desc = data["descripcion"]
            i_aux = data["auxiliar"]
            i_cuentadb = data["cuentaDB"]
            i_cuentacr = data["cuentaCR"]
            i_amount = data["monto"]

            # Llamamos el procedure usando las variables
            cursor.callproc(
                "proc_insert_entries",
                [i_desc, i_aux, i_cuentadb, i_cuentacr, i_amount],
            )

            # Commit del insert
            conn.commit()

            # Excepcion si el procedure no ejecuta
            return jsonify(
                {"message": "Asiento contable registrado correctamente.", "exito": True}
            ), 200

        else:
            return jsonify({"mensaje": "Parametros no correctos.", "exito": False})

    except cx_Oracle.DatabaseError as e:
        error = e.args[0]
        error_message = error.message.split("\n")[0]
        error_message = error_message.split(": ", 1)[1] if ": " in error_message else error_message

        # Excepciones que se parametrizaron en el procedure
        if error.code == 20001:
            return jsonify({"mensaje": error_message, "exito": False}), 403
        elif error.code == 20002:
            return jsonify({"mensaje": error_message, "exito": False}), 403
        elif error.code == 20003:
            return jsonify({"mensaje": error_message, "exito": False}), 403
        else:
            # Si es un error que el procedure no aguanta
            print(error)
            return jsonify(
                {
                    "mensaje": "Error desconocido al registrar el movimiento.",
                    "exito": False,
                }
            ), 400
    # Excepcion si el error es que no envio todos los parametros
    except Exception as ex:
        return jsonify(
            {"mensaje": "Error al registrar el movimiento.", "exito": False}
        ), 400

def pagina_no_encontrada(error):
    return "<h4>Por favor utilice un endpoint correcto. API Público de Contabilidad por Ian Fernández (A00100600) y Raymer Segura (A00104796).</h4>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host="0.0.0.0", port=int("5000"))