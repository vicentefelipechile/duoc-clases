/*======== CREAR TABLA EMPLEADOS ========*/
CREATE TABLE EMPLEADO (
    id_empleado NUMBER(6) CONSTRAINT empleado_pk PRIMARY KEY NOT NULL,
    primer_nombre VARCHAR2(25) NOT NULL,
    segundo_nombre VARCHAR2(25),
    apell_paterno VARCHAR2(25) NOT NULL,
    apell_materno VARCHAR2(25) NOT NULL,
    fecha_contrato DATE NOT NULL
);

/*======== CREAR TABLA EMPLEADOS ========*/
CREATE TABLE CLIENTE (
    id_cliente NUMBER(5) CONSTRAINT cliente_pk PRIMARY KEY NOT NULL,
    primer_nombre VARCHAR2(25) NOT NULL,
    segundo_nombre VARCHAR2(25),
    apell_paterno VARCHAR2(25) NOT NULL,
    apell_materno VARCHAR2(25) NOT NULL,
    direccion VARCHAR(30) NOT NULL
);

/*========= CREAR TABLA PEDIDO ==========*/
CREATE TABLE PEDIDO (
    nro_pedido NUMBER(6) CONSTRAINT pedido_pk PRIMARY KEY,
    fecha DATE NOT NULL,
    fecha_entrega DATE NOT NULL
);

ALTER TABLE PEDIDO DROP ( fecha_entrega );
ALTER TABLE PEDIDO ADD (
    fecha_entrega DATE,
    nombre VARCHAR2(20),
    direccion VARCHAR(20),
    fono NUMBER(5),
    peso NUMBER(3, 1)
);

/*====================================*/