CREATE DATABASE theamUdg;
/* userName se cambia por el usuario de la base que tengan */
CREATE USER 'userName'@'localhost' IDENTIFIED BY 'userName';
/* La contraeña se cambia por 'password', cambienla si quieren */
ALTER USER userName@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mekno.* TO 'userName'@'localhost';
USE theamUdg;

CREATE TABLE usuario(
    codigo INT UNSIGNED NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    sNombres VARCHAR(200) NOT NULL,
    apellidoP VARCHAR(100) NOT NULL,
    apellidoM VARCHAR(100) NOT NULL,
    carrera VARCHAR(100) NOT NULL,
    adminKey BOOLEAN DEFAULT FALSE,
    cicloInicio VARCHAR(50) NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    contrasenia VARCHAR(100) NOT NULL,
    PRIMARY KEY(codigo)
);

CREATE TABLE clase(
    clave VARCHAR(20) NOT NULL,
    fechaI VARCHAR(20) NOT NULL,
    fechaF VARCHAR(20) NOT NULL,
    creditos INT DEFAULT 1,
    PRIMARY KEY(clave)
);

CREATE TABLE materia(
    claseNrc INT UNSIGNED NOT NULL,
    clave VARCHAR(20) NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    dias VARCHAR(20) NOT NULL,
    seccion VARCHAR(5) NOT NULL,
    cupos INT DEFAULT 0,
    cupDis INT DEFAULT 0,
    edificio VARCHAR(20) NOT NULL,
    aula VARCHAR(20) NOT NULL,
    profesor VARCHAR (500),
    PRIMARY KEY (claseNrc),
    FOREIGN KEY (clave)
        REFERENCES clase(clave)
);

CREATE TABLE materiaAlumno(
    codigoAl INT UNSIGNED NOT NULL,
    claseNrc INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigoAl)
        REFERENCES usuario(codigo),
    FOREIGN KEY (claseNrc)
        REFERENCES materia (claseNrc) 
);

CREATE TABLE circulares(
    id INT UNSIGNED NOT NULL,
    contenido VARCHAR(300) NOT NULL,
    numero INT NOT NULL,
    fecha VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);