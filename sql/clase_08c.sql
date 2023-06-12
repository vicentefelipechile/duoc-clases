SELECT
    employee_id  AS "Empleado ID",
    job_id       AS "ID Trabajo",
    first_name   AS "Primer Nombre",
    last_name    AS "Apellido",
    salary       AS "Remuneracion",
    phone_number AS "Numero de telefono"
FROM
    employees
ORDER BY
    job_id DESC;
