-- Check and show privileges for user_0d_1
SELECT IF(COUNT(*) = 1, 'Exists', 'Does not exist') AS user_status
FROM mysql.user
WHERE user = 'user_0d_1' AND host = 'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check and show privileges for user_0d_2
SELECT IF(COUNT(*) = 1, 'Exists', 'Does not exist') AS user_status
FROM mysql.user
WHERE user = 'user_0d_2' AND host = 'localhost';

SHOW GRANTS FOR 'user_0d_2'@'localhost';
