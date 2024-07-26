-- Create the users if they do not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant all privileges to the users
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Flush the privileges to ensure that they are saved and available in the current session
FLUSH PRIVILEGES;

-- List the privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List the privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
