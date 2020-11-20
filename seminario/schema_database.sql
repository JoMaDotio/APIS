CREATE DATABASE typing_Game;
/* userName se cambia por el usuario de la base que tengan */
CREATE USER 'userName'@'localhost' IDENTIFIED BY 'userName';
/* La contraeña se cambia por 'password', cambienla si quieren */
ALTER USER userName@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON typing_game.* TO 'userName'@'localhost';
USE typing_game;

CREATE TABLE randomText (
    id INT NOT NULL PRIMARY KEY,
    contents VARCHAR (1000) NOT NULL
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
    FOREIGN KEY (idLess)
        REFERENCES lesson(numLess),
    FOREIGN KEY (idRand)
        REFERENCES randomText(id)
);