import psycopg2

crecacion_database_tablas = """
CREATE TABLE IF NOT EXISTS CENTROS_HOSPITALARIOS(
    id_hospital primary key int,
    nombre varchar(100)
);

CREATE TABLE IF NOT EXISTS GASTOS(
    id_gastos primary key serial, 
    id_hospital int not null,
    anio numeric,
    totalcompra numeric,
    producfarma numeric,
    materialsani numeric,
    implantes numeric,
    restomateriasani numeric,
    servcontratado numeric,
    trabajocontratado numeric,
    xrestocompras numeric,
    variaexistencias numeric,
    servexteriores numeric,
    sumistro numeric,
    xrestoserviexter numeric,
    gastopersonal numeric,
    sueldos numeric,
    indemnizacion numeric,
    segsocempresa numeric,
    otrgassocial numeric,
    dotaamortizacion numeric,
    perdidadeterioro numeric,
    xrestogasto numeric,
    totcompragasto numeric,
    foreign key (id_hospital)
        references (CENTROS_HOSPITALARIOS)
);

CREATE TABLE IF NOT EXISTS TIPOS_HOSPITALIZACION(
    id_tipo primary key,
    nombre varchar(100)
);

CREATE TABLE  IF NOT EXISTS INGRESOS(
    id_ingreso SERIAL not null,
    particulares NUMERIC(10,2),
    aseguradoras NUMERIC(10,2),
    aseguradoras_enfermedad NUMERIC(10,2),
    aseguradoreas_trafico NUMERIC(10,2),
    mutuas NUMERIC(10,2),
    id_tipo INT not null,
    año INT not null,
    id_hospital INT not null,
    foreign key (id_tipo)
        references TIPOS_HOSPITALIZACION(id_tipo),
    foreign key (id_hospital)
        references CENTROS_HOSPITALARIOS(id_hospital)
    );
"""