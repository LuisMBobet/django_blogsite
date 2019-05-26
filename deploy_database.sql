CREATE DATABASE Blogsite_db;
CREATE USER 'Bloguser'@'localhost' IDENTIFIED BY 'Blogpassword';
GRANT ALL PRIVILEGES ON Blogsite_db.* TO 'Bloguser'@'localhost';
FLUSH PRIVILEGES;
ALTER DATABASE Blogsite_db CHARACTER SET utf8;
