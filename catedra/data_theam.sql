USE theamUdg;
INSERT INTO usuario (codigo, nombre, apellidoP, apellidoM, carrera, adminKey, cicloInicio, activo, contrasenia)
    VALUES (215476966, 'Jose Manuel', 'Sanches', 'Fregoso', 'INCO', false, '2018B', true, 'holamundo');
INSERT INTO usuario (codigo, nombre, apellidoP, apellidoM, carrera, adminKey, cicloInicio, activo, contrasenia)
    VALUES (2154788584, 'Joaqin Atanasio', 'Del niño jesus', 'Pobrecito', 'INCO', false, '2019A', true, 'soyjoaqin');

INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I5884', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I7023', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I5890', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I7036', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I5897', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I5886', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I5888', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I7022', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I5898', '07/09/20', '18/12/20', 8);
INSERT INTO clase (clave, fechaI, fechaF, creditos)
    VALUES ('I7026', '07/09/20', '18/12/20', 8);

INSERT INTO materia (nrc, clave, materia, dias, horario, seccion, cupos, cuposDis, edificio, aula, profesor, ciclo, centro)
    VALUES (42268, 'I5884', 'ALGORITMIA', 'M,J', "7000-8055", 'D01', 42, 42, 'DEDX', 'A017', 'LUPERCIO CORONEL, RAMIRO', '2020B', 'CUCEI');
INSERT INTO materia (nrc, clave, materia, dias, horario, seccion, cupos, cuposDis, edificio, aula, profesor, ciclo, centro)
    VALUES (42269, 'I5884', 'ALGORITMIA', 'M,J', "9000-1055", 'D02', 42, 42, 'UNDEF', ' ', 'GARCIA HERNANDEZ MARTIN', '2020B', 'CUCEI');
INSERT INTO materia (nrc, clave, materia, dias, horario, seccion, cupos, cuposDis, edificio, aula, profesor, ciclo, centro)
    VALUES (59549, 'I5884', 'ALGORITMIA', 'M,J', "1100-1255", 'D06', 42, 42, 'DEDX', 'A003', 'ESPINOZA VALDEZ AURORA', '2020B', 'CUCEI');
INSERT INTO materia (nrc, clave, materia, dias, horario, seccion, cupos, cuposDis, edificio, aula, profesor, ciclo, centro)
    VALUES (59829, 'I5884', 'ALGORITMIA', 'M,J', "1300-1455", 'D10', 42, 42, 'DEDX', 'A002', 'GOMEZ ANAYA DAVID ALEJANDRO', '2020B', 'CUCEI');
INSERT INTO materia (nrc, clave, materia, dias, horario, seccion, cupos, cuposDis, edificio, aula, profesor, ciclo, centro)
    VALUES (140468, 'I5884', 'ALGORITMIA', 'L,I', "1500-1655",'D12', 42, 42, 'DEDX', 'A006', 'RODRIGUEZ ACOSTA, LUIS FERNANDO', '2020B', 'CUCEI');
INSERT INTO materia(nrc, clave, materia, dias, horario, seccion, cupos, cuposDis, edificio, aula, profesor, ciclo, centro)
    values(42261, "I7026", "TRADUCTORES DE LENGUAJES I", "L,I", "1300-1455", "D09", 24, 1, "DUCT2", "LC05", "MEZA ESPINOSA, JOSE JUAN", "2021A", "CUCEA");

INSERT INTO circulares (id, contenido, numero, fecha)
    VALUES (1,' Por acentroerdo con el Rector General y en seguimiento a las acciones preventivas que nuestra Institución ha llevado a cabo desde el 17 de marzo del año en centrorso para evitar la propagación del Coronavirus (Covid-19) y derivado del estado actual de la emergencia sanitaria, la Universidad de...', 31, '13/11/20');
INSERT INTO circulares (id, contenido, numero, fecha)
    VALUES (2,'Lunes 16 de noviembre (en conmemoración del 20 de noviembre), será día de descanso obligatorio tanto para el personal académico como para el personal administrativo; lo anterior, con base a lo estipulado en las cláusulas 33 y 61 de los Contratos Colectivos de Trabajo celebrados con el Sindicato...', 30, '10/11/20');
INSERT INTO circulares (id, contenido, numero, fecha)
    VALUES (3,'Por acentroerdo del Doctor Ricardo Villanueva Lomelí, Rector General de esta Casa de Estudios, les informo que el viernes 06 de noviembre del año en centrorso será día de descanso obligatorio exclusivamente para el personal administrativo; lo anterior, con base a lo estipulado en la cláusula 61 del...', 29, '03/11/20');
INSERT INTO circulares (id, contenido, numero, fecha)
    VALUES (4,'Por acentroerdo con el Rector General y en seguimiento a las acciones preventivas que nuestra Institución ha llevado a cabo desde el 17 de marzo del año en centrorso para evitar la propagación del Coronavirus (Covid-19) y derivado del estado actual de la emergencia sanitaria, la Universidad de...', 28, '30/10/20');
INSERT INTO circulares (id, contenido, numero, fecha)
    VALUES (5,'Lunes 02 de noviembre, será día de descanso obligatorio tanto para el personal académico como para el personal administrativo; lo anterior, con base a lo estipulado en las cláusulas 33 y 61 de los Contratos Colectivos de Trabajo celebrados con el STAUdeG y SUTUdeG, respectivamente.', 27, '23/10/20');
INSERT INTO circulares (id, contenido, numero, fecha)
    VALUES (6,'Por acentroerdo con el Rector General y en seguimiento a las acciones preventivas que nuestra Institución ha llevado a cabo desde el 17 de marzo del año en centrorso para evitar la propagación del Coronavirus (Covid-19) y derivado del estado actual de la Emergencia Sanitaria, la Universidad de...', 26, '09/10/20');

INSERT INTO materiaAlumno (codigo, nrc)
    VALUES(215476966, 59829);
INSERT INTO materiaAlumno (codigo, nrc)
    VALUES(215476966, 140468);
INSERT INTO materiaAlumno (codigo, nrc)
    VALUES(215476966, 42269);
