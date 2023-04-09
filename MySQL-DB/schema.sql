DROP DATABASE IF EXISTS flask_blog;

CREATE DATABASE flask_blog;

USE flask_blog;

DROP TABLE IF EXISTS tbl_user;
DROP TABLE IF EXISTS posts;

CREATE TABLE tbl_user (
  user_id INT NOT NULL AUTO_INCREMENT,
  user_name VARCHAR(45) NULL,
  user_username VARCHAR(45) NULL,
  user_password VARCHAR(45) NULL,
  PRIMARY KEY (user_id),
  UNIQUE (user_username)
);

-- INSERT INTO tbl_user (user_name, user_username, user_password) VALUES ('Alex', 'user_alex', '1234');
-- INSERT INTO tbl_user (user_name, user_username, user_password) VALUES ('Manuel', 'user_alex', '5678');
-- INSERT INTO tbl_user (user_name, user_username, user_password) VALUES ('Pedro', 'user_alex', '8910');

CREATE TABLE posts (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES tbl_user(user_id)
);

-- INSERT INTO posts (title, content) VALUES ( 'Post de Comida', 'Comidas ricas');
-- INSERT INTO posts (title, content) VALUES ( 'Post de Ropa', 'Ropa a la moda');
-- INSERT INTO posts (title, content) VALUES ( 'Post de Coches', 'Coches lentos');
