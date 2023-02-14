DELIMITER $$
CREATE TRIGGER after_order_update
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NEW.order_status = 1 THEN
        INSERT INTO orderLogs(order_type, order_log_date, order_log_num, order_log_item)
        VALUES (1, NOW(), NEW.order_num, NEW.order_item);
        
        SET NEW.order_purchasedate = NOW();
    END IF;

    IF NEW.order_status = 2 THEN
        INSERT INTO orderLogs(order_type, order_log_date, order_log_num, order_log_item)
        VALUES (2, NOW(), NEW.order_num, NEW.order_item);
        
        SET NEW.order_instockdate = NOW();
    END IF;

    IF NEW.order_status = 3 THEN
        INSERT INTO orderLogs(order_type, order_log_date, order_log_num, order_log_item)
        VALUES (3, NOW(), NEW.order_num, NEW.order_item);
        
        SET NEW.order_canceldate = NOW();
    END IF;
END $$
DELIMITER ;
