CREATE TABLE items(
    item_code INT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    item_remain INT NOT NULL,
    item_unit VARCHAR(50) NOT NULL,
    item_phone VARCHAR(50),
    item_email VARCHAR(50),
    item_img VARCHAR(255),
    item_manufact VARCHAR(50),
    item_price INT,
    item_descript TEXT
);

CREATE TABLE orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_item INT,
    order_num INT,
    order_unit VARCHAR(50),
    order_request_date DATE,
    order_placeorder BOOLEAN,
    order_placeorder_date DATE,
    order_instock_date DATE,
    order_instock BOOLEAN,

    CONSTRAINT FOREIGN KEY(order_item) REFERENCES items(item_code)

    ON DELETE CASCADE
    
);

CREATE TABLE accounts(
    account_id VARCHAR(10) PRIMARY KEY,
    account_name VARCHAR(10) NOT NULL,
    account_passwd VARCHAR(255),
    account_order BOOLEAN ,
    account_instock BOOLEAN,
    account_item BOOLEAN,
    account_management BOOLEAN
    
);