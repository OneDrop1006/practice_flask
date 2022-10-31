DB Schema commands

#データベース作成
CREATE DATABASE flashcard;

#DB選択
USE flashcard;

#テーブル作成
CREATE TABLE users (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,name varchar(255), favorite INT, done INT);

CREATE TABLE cards (id INT AUTO_INCREMENT PRIMARY KEY, word varchar(255), meaning varchar(255), category INT);

CREATE TABLE categories (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255));
