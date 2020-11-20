Ass root:
CREATE DATABASE typing_Game;
GRANT ALL PRIVILEGES ON typing_game.* TO 'userName'@'localhost';
In user profile:
Use typing_game;
CREATE TABLE randomText (
    id INT NOT NULL PRIMARY KEY,
    contenido VARCHAR (1000) NOT NULL
);

CREATE TABLE lesson ( 
    numLess INT UNSIGNED NOT NULL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL, 
    explanation VARCHAR (1000) NOT NULL, 
    category VARCHAR(500) 
);

CREATE TABLE lessRand (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    idLess INT UNSIGNED NOT NULL,
    idRand INT NOT NULL,
    FOREIGN KEY (idLess) REFERENCES lesson(numLess),
    FOREIGN KEY (idRand) REFERENCES randomText(id)
);