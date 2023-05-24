/*---------------------------------------------------------------------*/

CREATE TABLE super_heroe (
    id_super_heroe NUMBER(3) NOT NULL,
    nombre         VARCHAR2(20) NOT NULL,
    apellido       VARCHAR2(20) NOT NULL,
    ciudad         VARCHAR2(20) NOT NULL,
    apodo          VARCHAR2(20)
);

ALTER TABLE super_heroe ADD CONSTRAINT super_heroe_pk PRIMARY KEY ( id_super_heroe );

CREATE TABLE villano (
    id_villano                 NUMBER(3) NOT NULL,
    apodo                      VARCHAR2(32) NOT NULL,
    super_heroe_id_super_heroe NUMBER(3) NOT NULL
);

ALTER TABLE villano ADD CONSTRAINT villano_pk PRIMARY KEY ( id_villano );

ALTER TABLE villano
    ADD CONSTRAINT villano_super_heroe_fk FOREIGN KEY ( super_heroe_id_super_heroe )
        REFERENCES super_heroe ( id_super_heroe );

/*---------------------------------------------------------------------*/

INSERT INTO super_heroe VALUES (1, 'Karil', 'Giuseppe', 'Bere Alston', 'Andrew Chord');
INSERT INTO super_heroe VALUES (2, 'Loni', 'Devlin', 'Otopeni', 'Chase');
INSERT INTO super_heroe VALUES (3, 'Blondelle', 'Early', 'Kunagota', 'New Mutants');
INSERT INTO super_heroe VALUES (4, 'Edin', 'Hyman', 'Calubcub Dos', 'Mephisto');
INSERT INTO super_heroe VALUES (5, 'Heath', 'Tabor', 'Santiago', 'Kree');

/*---------------------------------------------------------------------*/


INSERT INTO villano VALUES (1, 'Baroness S.Bak', 2);
INSERT INTO villano VALUES (2, 'HYDRA', 1);      
INSERT INTO villano VALUES (3, 'Velocity', 1);   
INSERT INTO villano VALUES (4, 'Barracuda', 3);  
INSERT INTO villano VALUES (5, 'Solo', 1);       
INSERT INTO villano VALUES (6, 'Blue Beetle', 4);

/*---------------------------------------------------------------------*/
