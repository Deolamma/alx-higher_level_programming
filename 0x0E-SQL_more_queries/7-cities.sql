-- Creating a database that contains both foreign and private keys
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS cities(
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
