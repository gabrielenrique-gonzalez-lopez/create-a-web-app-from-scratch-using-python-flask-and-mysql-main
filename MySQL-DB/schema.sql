DROP DATABASE IF EXISTS flask_blog;

CREATE DATABASE flask_blog;

USE flask_blog;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE tbl_user (
  user_id BIGINT NULL AUTO_INCREMENT,
  user_name VARCHAR(45) NULL,
  user_username VARCHAR(45) NULL,
  user_password VARCHAR(45) NULL,
  PRIMARY KEY (user_id)
  UNIQUE (user_username)
);

-- INSERT INTO tbl_user (user_name, user_username, user_password) VALUES ('Alex', 'user_alex', '1234');
-- INSERT INTO tbl_user (user_name, user_username, user_password) VALUES ('Manuel', 'user_alex', '5678');
-- INSERT INTO tbl_user (user_name, user_username, user_password) VALUES ('Pedro', 'user_alex', '8910');

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES tbl_user(user_id)
);

-- INSERT INTO posts (title, content) VALUES ( 'Post de Comida', 'Comidas ricas');
-- INSERT INTO posts (title, content) VALUES ( 'Post de Ropa', 'Ropa a la moda');
-- INSERT INTO posts (title, content) VALUES ( 'Post de Coches', 'Coches lentos');

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;
