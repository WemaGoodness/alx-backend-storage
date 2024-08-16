-- Create a trigger to update item quantity after inserting a new order
DELIMITER //
CREATE TRIGGER DecreaseQuantityAfterOrder
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
