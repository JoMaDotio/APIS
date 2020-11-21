USE typing_game;
INSERT INTO randomText (id, contents)
    VALUES (1, "Aunque la gente feliz digan que lo son, nadie esta satisfecho: siempre tenemos que estar con la mujer mas hermosa, con la casa mas grande, cambiando coches, deseando lo que no tenemos.");
INSERT INTO randomText (id, contents)
    VALUES (2, "Creo que la iluminacion o revelacion vienen en la vida diaria. Busco el disfrute, la paz de la accion. Necesitas actuar. Hubiera parado de escribir hace años si fuese por el dinero");
INSERT INTO randomText (id, contents)
    VALUES (3, "La cosa mas importante en todas las relaciones humanas es la conversacion, pero la gente ya no habla, no se sientan y escuchan. Van al cine, al teatro, ven la television, escuchan la radio, leen libros, pero casi no hablan. Si queremos cambiar el mundo, tenemos que volver al tiempo en que los guerreros se sentaban alrededor de un fuego a contar historias");
INSERT INTO randomText (id, contents)
    VALUES (4, "Un niño puede enseñar a un adulto tres cosas: ser feliz sin razon, siempre estar ocupado con algo y saber como demandar con toda su voluntad lo que desea");
INSERT INTO randomText (id, contents)
    VALUES (5, "No permitas que tu mente le diga a tu corazon que debe hacer");

INSERT INTO lesson 
    VALUES (1, "Home Row", "Posiciona tus dedos sobre la fila central del teclado", "a-ñ");
INSERT INTO lesson 
    VALUES (2, "Top Row", "Posiciona tus dedos sobre la fila superior del teclado", "q-p");
INSERT INTO lesson 
    VALUES (3, "Bottom Row", "Posiciona tus dedos sobre la fila inferior del teclado", "z-""-""");
INSERT INTO lesson 
    VALUES (4, "Numeric Row", "Posiciona tus dedos sobre la fila numérica del teclado", "1-0");

INSERT INTO lessRand (idLess, idRand)
    VALUES (1, 1);
INSERT INTO lessRand (idLess, idRand)
    VALUES (1, 2);
INSERT INTO lessRand (idLess, idRand)
    VALUES (2, 3);
INSERT INTO lessRand (idLess, idRand)
    VALUES (3, 4);
INSERT INTO lessRand (idLess, idRand)
    VALUES (4, 5);

INSERT INTO ranking
    VALUES ("ElOaks", 72);
INSERT INTO ranking
    VALUES ("AngelogroPistaches", 73);
INSERT INTO ranking
    VALUES ("ElGrobas", 69);
INSERT INTO ranking
    VALUES ("Mañuel", 70);
INSERT INTO ranking
    VALUES ("SilisiosElDelFarnais", 66);
INSERT INTO ranking
    VALUES ("DieguitoMaradona", 75);