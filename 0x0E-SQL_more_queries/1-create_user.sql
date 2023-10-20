-- Creating a root user on a database
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED WITH caching_sha2_plugin BY "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost WITH GRANT;
