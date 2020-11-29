CREATE DATABASE theamUdg;
/* userName se cambia por el usuario de la base que tengan */
CREATE USER 'userName'@'localhost' IDENTIFIED BY 'userName';
/* La contraeña se cambia por 'password', cambienla si quieren */
ALTER USER userName@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON theamUdg.* TO 'userName'@'localhost';
USE theamUdg;

CREATE TABLE usuario(
    codigo INT UNSIGNED NOT NULL,
    nombre VARCHAR(250) NOT NULL,
    apellidoP VARCHAR(100) NOT NULL,
    apellidoM VARCHAR(100) NOT NULL,
    carrera VARCHAR(100) NOT NULL,
    cicloInicio VARCHAR(50) NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    adminKey BOOLEAN DEFAULT FALSE,
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
    nrc INT UNSIGNED NOT NULL,
    clave VARCHAR(20) NOT NULL,
    materia VARCHAR(150) NOT NULL,
    seccion VARCHAR(5) NOT NULL,
    horario VARCHAR(10) NOT NULL,
    dias VARCHAR(20) NOT NULL,
    edificio VARCHAR(20) NOT NULL,
    aula VARCHAR(20) NOT NULL,
    profesor VARCHAR (500) NOT NULL,
    cupos INT DEFAULT 0,
    cuposDis INT DEFAULT 0,
    ciclo VARCHAR (10) NOT NULL,
    centro VARCHAR (100) NOT NULL,
    PRIMARY KEY (nrc),
    FOREIGN KEY (clave)
        REFERENCES clase(clave)
);

CREATE TABLE materiaAlumno(
    codigo INT UNSIGNED NOT NULL,
    nrc INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo)
        REFERENCES usuario(codigo),
    FOREIGN KEY (nrc)
        REFERENCES materia (nrc)
);

CREATE TABLE circulares(
    id INT UNSIGNED NOT NULL,
    contenido VARCHAR(400) NOT NULL,
    numero INT NOT NULL,
    fecha VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);