-- This script creates a trigger to reset `valid_email` when the email changes
DELIMITER $$
CREATE TRIGGER reset_valid_email 
BEFORE UPDATE ON users 
FOR EACH ROW 
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;
