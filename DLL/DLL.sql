-- TABLES

CREATE TABLE acc_types (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR2(255),
    orig VARCHAR2(2) CHECK (orig in ('DB', 'CR')),
    status VARCHAR2(255)
);

CREATE TABLE aux_systems (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(255),
    status VARCHAR2(255)
);

CREATE TABLE accounting_accs (
    id NUMBER PRIMARY KEY,
    description VARCHAR2(255),
    acc_types NUMBER REFERENCES acc_types(id),
    trx_allowed CHAR(1) CHECK (trx_allowed IN ('N', 'Y')),
    acc_level NUMBER CHECK (acc_level IN (1, 2, 3)),
    general_acc NUMBER,
    balance NUMBER,
    status VARCHAR2(255)
);

CREATE TABLE currency (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description VARCHAR2(255),
    rate NUMBER,
    status VARCHAR2(255)
);

CREATE TABLE accounting_entries (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    descrip VARCHAR2(255),
    aux_id NUMBER REFERENCES aux_systems(id),
    accs_id NUMBER REFERENCES accounting_accs(id), 
    mov_type VARCHAR2(2) CHECK (mov_type IN ('CR', 'DB')),
    entry_date DATE,
    amount NUMBER,
    status VARCHAR2(255)
);

CREATE TABLE cont_users (
    username VARCHAR2(255) PRIMARY KEY,
    pass VARCHAR2(255)
);

-- DATA
-- acc_types data
INSERT INTO acc_types (description, orig, status) VALUES ('Activos', 'DB', '1');
INSERT INTO acc_types (description, orig, status) VALUES ('Pasivos', 'CR', '1');
INSERT INTO acc_types (description, orig, status) VALUES ('Capital', 'CR', '1');
INSERT INTO acc_types (description, orig, status) VALUES ('Ingresos', 'CR', '1');
INSERT INTO acc_types (description, orig, status) VALUES ('Costos', 'DB', '1');
INSERT INTO acc_types (description, orig, status) VALUES ('Gastos', 'DB', '1');

-- currency data
INSERT INTO currency (description, rate, status) VALUES ('DOP', 1, '1');
INSERT INTO currency (description, rate, status) VALUES ('USD', 45.87, '1');
INSERT INTO currency (description, rate, status) VALUES ('EUR', 57.89, '1');

-- aux_systems data
INSERT INTO aux_systems (name, status) VALUES ('Contabilidad', '1');
INSERT INTO aux_systems (name, status) VALUES ('Nomina', '1');
INSERT INTO aux_systems (name, status) VALUES ('Facturacion', '1');
INSERT INTO aux_systems (name, status) VALUES ('Inventario', '1');
INSERT INTO aux_systems (name, status) VALUES ('Cuentas x Cobrar', '1');
INSERT INTO aux_systems (name, status) VALUES ('Cuentas x Pagar', '1');
INSERT INTO aux_systems (name, status) VALUES ('Compras', '1');
INSERT INTO aux_systems (name, status) VALUES ('Activos Fijos', '1');
INSERT INTO aux_systems (name, status) VALUES ('Cheques', '1');

-- accounting_accs data
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (1, 'Activos', 'N', 1, 1, 0, NULL, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (2, 'Efectivo en caja y banco', 'N', 1, 2, 0, 1, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (3, 'Caja Chica', 'Y', 1, 3, 0, 2, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (4, 'Cuenta Corriente Banco X', 'Y', 1, 3, 0, 3, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (5, 'Inventarios y Mercancias', 'N', 1, 2, 0, 1, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (6, 'Inventario', 'Y', 1, 3, 0, 5, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (7, 'Cuentas x Cobrar', 'N', 1, 2, 0, 1, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (8, 'Cuentas x Cobrar Cliente X', 'Y', 1, 3, 0, 7, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (12, 'Ventas', 'N', 4, 2, 0, 9, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (13, 'Ingresos x Ventas', 'Y', 4, 3, 0, 12, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (47, 'Gastos', 'N', 6, 1, 0, NULL, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (48, 'Gastos Administrativos', 'N', 6, 2, 0, 47, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (50, 'Gastos Generales', 'Y', 6, 3, 0, 48, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (65, 'Gasto depreciación Activos Fijos', 'N', 6, 2, 0, 47, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (66, 'Depreciación Acumulada Activos Fijos', 'Y', 6, 3, 0, 65, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (70, 'Salarios y Sueldos Empleados', 'Y', 2, 3, 0, 18, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (71, 'Gastos de Nomina Empresa', 'Y', 6, 3, 0, 58, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (80, 'Compra de Mercancias', 'Y', 5, 3, 0, 78, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (81, 'Cuentas x Pagar', 'N', 2, 2, 0, 19, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (82, 'Cuentas x Pagar Proveedor X', 'Y', 2, 3, 0, 81, '1');
INSERT INTO accounting_accs (id, description, trx_allowed, acc_types, acc_level, balance, general_acc, status) VALUES (83, 'Cuentas Cheques en Banco X', 'Y', 1, 3, 0, 3, '1');

-- cont_users
INSERT INTO cont_users(username, pass) VALUES('admin', 'admin');

-- Stored procedure

CREATE OR REPLACE PROCEDURE proc_insert_accounting_accs(
  i_id NUMBER,
  i_desc VARCHAR2,
  i_acc_type VARCHAR2,
  i_trx_allowed VARCHAR2,
  i_acc_lvl NUMBER,
  i_gnl_acc VARCHAR2,
  i_bln NUMBER,
  i_status VARCHAR2
)
IS
  v_acctype VARCHAR2(30);
  v_trx_allowed VARCHAR2(1);
  v_gnl_acc NUMBER;
  v_status VARCHAR2(1);
  acc_type_not_found EXCEPTION;
  general_acc_not_found EXCEPTION;
BEGIN
  BEGIN
    SELECT id INTO v_acctype FROM acc_types WHERE description = i_acc_type;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE acc_type_not_found;
  END;
  
  IF i_trx_allowed = 'Si' THEN
    v_trx_allowed := 'Y';
  ELSE
    v_trx_allowed := 'N';
  END IF;
  
  BEGIN
    SELECT id INTO v_gnl_acc FROM accounting_accs WHERE description = i_gnl_acc;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE general_acc_not_found;
  END;
  
  IF i_status = 'Activado' THEN
    v_status := '1';
  ELSE
    v_status := '0';
  END IF;
  
  INSERT INTO accounting_accs (id, description, acc_types, trx_allowed, acc_level, general_acc, balance, status)
  VALUES (i_id, i_desc, v_acctype, v_trx_allowed, i_acc_lvl, v_gnl_acc, i_bln, v_status);
  
  EXCEPTION
    WHEN acc_type_not_found THEN
      RAISE_APPLICATION_ERROR(-20001, 'Tipo de cuenta no existe');
    WHEN general_acc_not_found THEN
      RAISE_APPLICATION_ERROR(-20002, 'Cuenta general no existe');
    WHEN OTHERS THEN
      RAISE_APPLICATION_ERROR(-20003, 'Error desconocido');
END proc_insert_accounting_accs;
/

CREATE OR REPLACE PROCEDURE proc_insert_acctypes(
  i_desc VARCHAR2,
  i_orig VARCHAR2,
  i_status VARCHAR2
)
IS
  v_status VARCHAR2(1);
BEGIN
  IF i_status = 'Activado' THEN
    v_status := '1';
  ELSE
    v_status := '0';
  END IF;

  INSERT INTO acc_types (description, orig, status) VALUES (i_desc, i_orig, v_status);
END;
/

CREATE OR REPLACE PROCEDURE proc_insert_currency(
  i_desc VARCHAR2,
  i_rate VARCHAR2,
  i_status VARCHAR2
)
IS
  v_status VARCHAR2(1);
BEGIN
  IF i_status = 'Activado' THEN
    v_status := '1';
  ELSE
    v_status := '0';
  END IF;

    INSERT INTO currency (description, rate, status) VALUES (i_desc, i_rate, v_status);
END proc_insert_currency;
/

CREATE OR REPLACE PROCEDURE proc_insert_aux(
  i_name VARCHAR2,
  i_status VARCHAR2
)
IS
  v_status VARCHAR2(1);
BEGIN
  IF i_status = 'Activado' THEN
    v_status := '1';
  ELSE
    v_status := '0';
  END IF;

    INSERT INTO aux_systems (name, status) VALUES (i_name, v_status);
END proc_insert_aux;
/

CREATE OR REPLACE PROCEDURE proc_insert_entries(
  i_desc VARCHAR2,
  i_aux NUMBER,
  i_accdb NUMBER,
  i_acccr NUMBER,
  i_amount NUMBER
)
IS
  v_accdb NUMBER;
  v_acccr NUMBER;
  v_aux NUMBER;
  accdb_not_found EXCEPTION;
  acccr_not_found EXCEPTION;
  aux_not_found EXCEPTION;
BEGIN

  BEGIN
    SELECT id INTO v_accdb FROM accounting_accs WHERE id = i_accdb;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE accdb_not_found;
  END;

  BEGIN
    SELECT id INTO v_acccr FROM accounting_accs WHERE id = i_acccr;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE acccr_not_found;
  END;

  BEGIN
    SELECT id INTO v_aux FROM aux_systems WHERE id = i_aux;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE aux_not_found;
  END;
  
  INSERT INTO accounting_entries (descrip, aux_id, accs_id, mov_type, entry_date, amount, status)
  VALUES (i_desc, v_aux, v_accdb, 'DB', sysdate, i_amount, 'R');

  INSERT INTO accounting_entries (descrip, aux_id, accs_id, mov_type, entry_date, amount, status)
  VALUES (i_desc, v_aux, v_acccr, 'CR', sysdate, i_amount, 'R');
  
  EXCEPTION
    WHEN accdb_not_found THEN
      RAISE_APPLICATION_ERROR(-20001, 'Cuenta contable a hacer el débito no existe.');
    WHEN acccr_not_found THEN
      RAISE_APPLICATION_ERROR(-20002, 'Cuenta contable a hacer el crédito no existe.');
    WHEN aux_not_found THEN
      RAISE_APPLICATION_ERROR(-20003, 'Auxiliar contable no existe.');
    WHEN OTHERS THEN
      RAISE_APPLICATION_ERROR(-20004, 'Error desconocido');
END proc_insert_entries;
/

CREATE OR REPLACE PROCEDURE proc_insert_entries_gui(
  i_desc VARCHAR2,
  i_aux VARCHAR2,
  i_accdb VARCHAR2,
  i_mov VARCHAR2,
  i_amount NUMBER
)
IS
  v_accdb NUMBER;
  v_aux NUMBER;
  accdb_not_found EXCEPTION;
  acccr_not_found EXCEPTION;
  aux_not_found EXCEPTION;
BEGIN

  BEGIN
    SELECT id INTO v_accdb FROM accounting_accs WHERE description = i_accdb;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE accdb_not_found;
  END;

  BEGIN
    SELECT id INTO v_aux FROM aux_systems WHERE name = i_aux;
  EXCEPTION WHEN NO_DATA_FOUND THEN
    RAISE aux_not_found;
  END;
  
  INSERT INTO accounting_entries (descrip, aux_id, accs_id, mov_type, entry_date, amount, status)
  VALUES (i_desc, v_aux, v_accdb, i_mov, sysdate, i_amount, 'R');
  
  EXCEPTION
    WHEN accdb_not_found THEN
      RAISE_APPLICATION_ERROR(-20001, 'Cuenta contable no existe.');
    WHEN aux_not_found THEN
      RAISE_APPLICATION_ERROR(-20002, 'Auxiliar contable no existe.');
    WHEN OTHERS THEN
      RAISE_APPLICATION_ERROR(-20003, 'Error desconocido');
END proc_insert_entries_gui;
/

CREATE OR REPLACE PROCEDURE proc_check_credentials (
    i_username IN VARCHAR2,
    i_password IN VARCHAR2,
    o_result OUT VARCHAR2
) IS
    v_count NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_count FROM cont_users WHERE username = i_username AND pass = i_password;
    IF v_count = 1 THEN
        o_result := 'yes';
    ELSE
        o_result := 'no';
    END IF;
END;


-- Useful queries
EXEC proc_insert_accounting_accs(85,'Prueba','Activos','Si',1,'Caja Chica',1000.45,'Activado');
EXEC proc_insert_entries('Prueba asiento','Contabilidadd','Efectivo en caja y banco','Pasivos',1000.45);
EXEC proc_insert_entries('Prueba asiento',1,3,1,1000.45);

select * from acc_types;
select * from accounting_accs order by id desc;
select * from accounting_entries;
select * from aux_systems;
select * from currency;
select * from cont_users;

SELECT id, 
description,
(SELECT b.description FROM accounting_accs b WHERE b.id = a.acc_types) as acc_type,
CASE trx_allowed WHEN 'Y' THEN 'Si' ELSE 'No' END AS trx_allowed, 
acc_level,
COALESCE((SELECT b.description FROM accounting_accs b WHERE b.id = a.general_acc), a.description) as general,
balance, 
CASE status WHEN '1' THEN 'Activado' ELSE 'Desactivado' END AS status
FROM accounting_accs a order by id desc;

SELECT id, descrip,
(SELECT b.name FROM aux_systems b WHERE b.id = a.aux_id) as aux_id,
(SELECT c.description FROM accounting_accs c WHERE c.id = a.accs_id) as accs_id,
mov_type, entry_date, amount, status
FROM accounting_entries a;