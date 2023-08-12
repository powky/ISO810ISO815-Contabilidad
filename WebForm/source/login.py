from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dotenv import load_dotenv
import cx_Oracle
import subprocess
import os


class Ui_Contabilidad(object):

    def __init__(self, window):
        self.window = window
        load_dotenv()

    # Definición del UI 

    def setupUi(self, Contabilidad):
        Contabilidad.setObjectName("Contabilidad")
        Contabilidad.resize(400, 300)
        Contabilidad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Contabilidad.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textEdit = QtWidgets.QTextEdit(Contabilidad)
        self.textEdit.setGeometry(QtCore.QRect(110, 60, 181, 31))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Contabilidad)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 130, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(Contabilidad)
        self.pushButton.setGeometry(QtCore.QRect(110, 190, 181, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Contabilidad)
        self.label.setGeometry(QtCore.QRect(110, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Contabilidad)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 111, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Contabilidad)
        QtCore.QMetaObject.connectSlotsByName(Contabilidad)

    def retranslateUi(self, Contabilidad):
        _translate = QtCore.QCoreApplication.translate
        Contabilidad.setWindowTitle(_translate("Contabilidad", "Contabilidad ISO8XX - Ian/Raymer"))
        self.pushButton.setText(_translate("Contabilidad", "Acceder"))
        self.label.setText(_translate("Contabilidad", "Usuario"))
        self.label_2.setText(_translate("Contabilidad", "Contraseña"))

    # Función de inicio de sesión

    def login(self):

        username = self.textEdit.toPlainText()
        password = self.lineEdit_2.text() 

        # Conexión a la base de datos
        os.environ['TNS_ADMIN'] = os.getenv("ORA_ADMIN")
        connection = cx_Oracle.connect(os.getenv("ORA_USER"), os.getenv("ORA_PASS"), os.getenv("ORA_TNS"))
        cursor = connection.cursor()
        result = cursor.var(cx_Oracle.STRING)
        cursor.callproc("proc_check_credentials", [username, password, result]) # Consumir el Stored Procedure

        # Condicional a partir del resultado del Stored Procedure
        if result.getvalue() == 'yes':
            self.window.close() # Cerrar la ventana de este programa
            subprocess.Popen(["/usr/local/Cellar/python@3.9/3.9.17_1/bin/python3.9", "main.py"]) # Abrir programa principal de contabilidad
        else:
            QMessageBox.critical(None, "Error", "Su usuario o contraseña no es correcto.")

        # Cerrar conexión a la base de datos
        cursor.close()
        connection.close()


# Correr y asignar funciones al momento de correr el programa
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contabilidad = QtWidgets.QFrame()
    ui = Ui_Contabilidad(Contabilidad)
    ui.setupUi(Contabilidad)
    ui.pushButton.clicked.connect(ui.login)
    Contabilidad.show()
    sys.exit(app.exec_())
