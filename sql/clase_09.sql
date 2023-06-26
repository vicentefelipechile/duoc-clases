-- CREAR USUARIO

	-- USER SQL
	-- Contraseña larga debido a restricciones de la base de datos de oracle
	CREATE USER "VCORTES" IDENTIFIED BY "Btg.elpepeysusamigos2002"  
	DEFAULT TABLESPACE "SYSAUX"
	TEMPORARY TABLESPACE "TEMP";

	-- QUOTAS / Cuotas ilimitadas
	ALTER USER "VCORTES" QUOTA UNLIMITED ON "SYSTEM";
	ALTER USER "VCORTES" QUOTA UNLIMITED ON "DBFS_DATA";
	ALTER USER "VCORTES" QUOTA UNLIMITED ON "SAMPLESCHEMA";
	ALTER USER "VCORTES" QUOTA UNLIMITED ON "DATA";
	ALTER USER "VCORTES" QUOTA UNLIMITED ON "SYSAUX";

	-- ROLES / Privilegios
	GRANT "CONNECT" TO "VCORTES" ;
	GRANT "RESOURCE" TO "VCORTES" ;

	-- SYSTEM PRIVILEGES

-- FIN CREAR USUARIO



/*-----------------------------*/
/*------ CREAR SECUENCIAS -----*/
/*-----------------------------*/

CREATE SEQUENCE
    sequence_id_fabrica
START WITH 5
INCREMENT BY 5;

CREATE SEQUENCE
    sequence_id_boleta
START WITH 1010
INCREMENT BY 10;

CREATE SEQUENCE
    sequence_id_comuna
START WITH 5
INCREMENT BY 5;


/*-----------------------------*/
/*------ CREAR PRE-TABLAS -----*/
/*-----------------------------*/

CREATE TABLE boleta (
    id_boleta NUMBER(10) PRIMARY KEY NOT NULL,
    id_cliente NUMBER NOT NULL,
    id_empleado NUMBER NOT NULL,
    -- Al ingresar una boleta, ésta debe quedar registrada con la fecha de la base de datos.
    fecha_boleta DATE DEFAULT SYSDATE NOT NULL
);

CREATE TABLE cliente (
    id_cliente NUMBER PRIMARY KEY NOT NULL,
    nombre_cliente VARCHAR2(35) NOT NULL,
    direccion VARCHAR2(50) NOT NULL,
    telefono NUMBER(9) NOT NULL,
    id_comuna NUMBER(3) NOT NULL
);

CREATE TABLE comuna (
    -- Existen alrededor de 300 comunas en chile
    id_comuna NUMBER(3) PRIMARY KEY NOT NULL,
    nombre_comuna VARCHAR(30) NOT NULL
);


/*-----------------------------*/
/*-- CREAR PRE-RESTRICCIONES --*/
/*-----------------------------*/

ALTER TABLE
    boleta
ADD CONSTRAINT boleta_id_cliente_fk FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
MODIFY id_boleta DEFAULT sequence_id_boleta.NEXTVAL;

ALTER TABLE
    cliente
ADD CONSTRAINT cliente_id_comuna_fk FOREIGN KEY (id_comuna) REFERENCES comuna (id_comuna)
MODIFY id_comuna DEFAULT sequence_id_comuna.NEXTVAL;



/*-----------------------------*/
/*-------- CREAR TABLAS -------*/
/*-----------------------------*/

CREATE TABLE detalleboleta (
    id_detalle NUMBER(10) PRIMARY KEY NOT NULL,
    id_boleta NUMBER(10) NOT NULL,
    id_producto NUMBER(10) NOT NULL,
    cantidad NUMBER(3) NOT NULL
);

CREATE TABLE producto (
    id_producto NUMBER(10) PRIMARY KEY NOT NULL,
    nombre_producto VARCHAR2(25) NOT NULL,
    -- Los precios de los helados no deberian ser mayores a 99.999
    precio NUMBER(5) NOT NULL,
    stock_actual NUMBER(4) NOT NULL,
    stock_minimo NUMBER(4) NOT NULL,
    id_fabrica NUMBER(4) NOT NULL
);

CREATE TABLE fabrica (
    id_fabrica NUMBER(4) PRIMARY KEY NOT NULL,
    nombre_fabrica VARCHAR2(60) NOT NULL
);


CREATE TABLE equipo (
    -- Un unico caracter para ser identificado
    id_equipo CHAR(1) PRIMARY KEY NOT NULL,
    nombre_equipo VARCHAR2(10) NOT NULL,
    porcentaje NUMBER(3,2) NOT NULL
);

CREATE TABLE categorizacion (
    -- Un unico caracter para ser identificado
    id_categorizacion CHAR(1) PRIMARY KEY NOT NULL,
    nombre_categorizacion VARCHAR2(10) NOT NULL,
    porcentaje NUMBER(3,2) NOT NULL
);

CREATE TABLE empleado (
    id_empleado NUMBER(6) PRIMARY KEY NOT NULL,
    rut_empleado VARCHAR2(10) UNIQUE NOT NULL,
    primer_nombre VARCHAR(10) NOT NULL,
    segundo_nombre VARCHAR2(15),
    apell_paterno VARCHAR2(15) NOT NULL,
    apell_materno VARCHAR2(15),
    fecha_nac DATE NOT NULL,
    fecha_contrato DATE NOT NULL,
    sueldo NUMBER(9) NOT NULL,
    comision NUMBER NOT NULL,
    -- Unicos caracteres para ser identificado
    id_equipo CHAR(1),
    id_categorizacion CHAR(1) NOT NULL
);


/*-----------------------------*/
/*---- CREAR RESTRICCIONES ----*/
/*-----------------------------*/

-- El stock actual de un producto no puede ser igual o inferior al stock mínimo de ese producto.
ALTER TABLE
    producto
ADD CONSTRAINT producto_stock_actual_check CHECK (stock_actual >= stock_minimo);

-- Por acuerdo entre el sindicato y la gerencia de la empresa, a los empleados se les asignará una comisión entre 12% y 25%.
ALTER TABLE
    empleado
ADD CONSTRAINT empleado_comision_check CHECK (comision >= 0.12 AND comision <= 0.25);

ALTER TABLE
	empleado
ADD CONSTRAINT empleado_id_equipo_fk FOREIGN KEY (id_equipo) REFERENCES equipo (id_equipo)
ADD CONSTRAINT empleado_id_categorizacion_fk FOREIGN KEY (id_categorizacion) REFERENCES categorizacion (id_categorizacion);

ALTER TABLE
    boleta
ADD CONSTRAINT boleta_id_empleado_fk FOREIGN KEY (id_empleado) REFERENCES empleado (id_empleado);

ALTER TABLE
    detalleboleta
ADD CONSTRAINT detalleboleta_id_boleta_fk FOREIGN KEY (id_boleta) REFERENCES boleta (id_boleta)
ADD CONSTRAINT detalleboleta_id_producto_fk FOREIGN KEY (id_producto) REFERENCES producto (id_producto);

ALTER TABLE
    producto
ADD CONSTRAINT producto_id_fabrica_fk FOREIGN KEY (id_fabrica) REFERENCES fabrica (id_fabrica);


