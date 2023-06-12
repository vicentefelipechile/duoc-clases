/* ---------------------------- */
/* -- CREACION DE SECUENCIAS -- */
/* ---------------------------- */


CREATE SEQUENCE seq_id_arriendo START WITH 10 INCREMENT BY 10;
CREATE SEQUENCE seq_id_salud START WITH 300 INCREMENT BY 2;
CREATE SEQUENCE seq_id_comuna START WITH 0 INCREMENT BY 3;
CREATE SEQUENCE seq_empleado START WITH 100 INCREMENT BY 2;
CREATE SEQUENCE seq_cliente START WITH 200 INCREMENT BY 20;



/* ---------------------------- */
/* ---- CREACION DE TABLAS ---- */
/* ---------------------------- */


-- Primary key a nivel de tabla
CREATE TABLE arriendo_camion (
	id_arriendo NUMBER(7) PRIMARY KEY NOT NULL,
	nro_patente VARCHAR2(6) NOT NULL,
	numrun_cli NUMBER(10) NOT NULL,
	fecha_ini_arriendo VARCHAR(6) NOT NULL,
	dias_solicitados NUMBER(6),
	fecha_devolucion DATE
);

CREATE TABLE cliente (
	numrun_cli NUMBER(10) PRIMARY KEY NOT NULL,
	dvrun_cli VARCHAR2(1) NOT NULL,
	appaterno_cli VARCHAR2(30) NOT NULL,
	apmaterno_cli VARCHAR2(30) NOT NULL,
	pnombre_cli VARCHAR2(30) NOT NULL,
	snombre_cli VARCHAR2(30),
	direccion VARCHAR2(60) NOT NULL,
	celular NUMBER(15),
	fono_fijo_cli NUMBER(15),
	renta VARCHAR2(7) NOT NULL,
	fecha_nac_cli DATE,
	id_comuna NUMBER(3),
	id_tipo_cli VARCHAR2(2) NOT NULL,
	id_estado_civil NUMBER(1) NOT NULL,
	tipo_cliente VARCHAR2(15) NOT NULL
);

CREATE TABLE comuna (
	id_comuna NUMBER(3) PRIMARY KEY NOT NULL,
	nombre_comuna VARCHAR2(30)
);

CREATE TABLE camion (
	nro_patente VARCHAR2(6) PRIMARY KEY NOT NULL,
	color VARCHAR2(15) NOT NULL,
	motor VARCHAR2(5) NOT NULL,
	anio NUMBER(5),
	valor_arriendo_dia NUMBER(7) NOT NULL,
	valor_garantia_dia NUMBER(6),
	id_tipo_camion VARCHAR2(10) NOT NULL,
	numrun_emp NUMBER(10),
	id_marca NUMBER NOT NULL,
	tipo_camion VARCHAR2(40) NOT NULL,
	marca VARCHAR2(20) NOT NULL
);

CREATE TABLE empleado (
	numrun_emp NUMBER(10) PRIMARY KEY NOT NULL,
	dvrun_emp VARCHAR2(1) NOT NULL,
	appaterno_emp VARCHAR2(30) NOT NULL,
	apmaterno_emp VARCHAR2(30) NOT NULL,
	pnombre_emp VARCHAR2(25) NOT NULL,
	snombre_emp VARCHAR2(25),
	direccion_emp VARCHAR2(60) NOT NULL,
	sexo CHAR(1) NOT NULL,
	celular_emp NUMBER(15),
	fono_fijo_emp NUMBER(15),
	fecha_nac DATE NOT NULL,
	fecha_contrato DATE,
	sueldo_base NUMBER(7) NOT NULL,
	id_comuna NUMBER(3),
	id_tipo_sal VARCHAR2(3) NOT NULL,
	id_estado_civil NUMBER(1) NOT NULL
);

CREATE TABLE tipo_salud (
	id_tipo_sal VARCHAR2(3) PRIMARY KEY NOT NULL,
	descripcion VARCHAR2(100) NOT NULL,
	pct_sueldo NUMBER(3,1) NOT NULL
);

CREATE TABLE estado_civil (
	id_estado_civil NUMBER(1) PRIMARY KEY NOT NULL,
	estado_civil VARCHAR(25) NOT NULL
);



/* ---------------------------- */
/* -- CREACION DE RELACIONES -- */
/* ---------------------------- */



ALTER TABLE
	cliente
ADD CONSTRAINT cliente_id_comuna_fk FOREIGN KEY (id_comuna) REFERENCES comuna (id_comuna)
ADD CONSTRAINT cliente_id_estado_civil_fk FOREIGN KEY (id_estado_civil) REFERENCES estado_civil (id_estado_civil);


ALTER TABLE
	empleado
ADD CONSTRAINT empleado_id_tipo_sal_fk FOREIGN KEY (id_tipo_sal) REFERENCES tipo_salud (id_tipo_sal);


ALTER TABLE
	empleado
ADD CONSTRAINT empleado_id_estado_civil_fk FOREIGN KEY (id_estado_civil) REFERENCES estado_civil (id_estado_civil);


ALTER TABLE
	camion
ADD CONSTRAINT camion_numrun_emp_fk FOREIGN KEY (numrun_emp) REFERENCES empleado (numrun_emp)
ADD CONSTRAINT camion_valor_arriendo_dia_chk CHECK (valor_arriendo_dia > 0)
ADD CONSTRAINT camion_valor_garantia_dia_chk CHECK (valor_garantia_dia > 0);


ALTER TABLE
	arriendo_camion
ADD CONSTRAINT arriendo_camion_nro_patente_fk FOREIGN KEY (nro_patente) REFERENCES camion (nro_patente)
ADD CONSTRAINT arriendo_camion_numrun_cli_fk FOREIGN KEY (numrun_cli) REFERENCES cliente (numrun_cli)
ADD CONSTRAINT arriendo_camion_fecha_devolucion_chk CHECK (fecha_devolucion = DATE() );



/* ---------------------------- */
/* ------- ELIMINAR TODO ------ */
/* ---------------------------- *



DROP TABLE arriendo_camion CASCADE CONSTRAINTS;
DROP TABLE camion CASCADE CONSTRAINTS;
DROP TABLE cliente CASCADE CONSTRAINTS;
DROP TABLE comuna CASCADE CONSTRAINTS;
DROP TABLE empleado CASCADE CONSTRAINTS;
DROP TABLE estado_civil CASCADE CONSTRAINTS;
DROP TABLE tipo_salud CASCADE CONSTRAINTS;



/* ---------------------------- */
/* ------- ELIMINAR TODO ------ */
/* ---------------------------- */
