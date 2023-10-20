-- Creating a primmary key
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS states(
	id INT AUTO_INCREMENT UNIQUE NOT NULL, 
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);
