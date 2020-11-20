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

Create table demo (
    id INT PRIMARY KEY,
    randText INT NOT NULL,
    FOREIGN KEY (randText)
        REFERENCES randomText(id));