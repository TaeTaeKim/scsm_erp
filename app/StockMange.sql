CREATE TABLE items(
    item_code INT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    item_stock FLOAT(7,2) NOT NULL,
    item_unit VARCHAR(50) NOT NULL,
    item_manufact VARCHAR(50),
    item_phone VARCHAR(50),
    item_email VARCHAR(50),
    item_img VARCHAR(255),
    item_price INT,
    item_descript TEXT
);

CREATE TABLE orders(
    order_id VARCHAR(50) PRIMARY KEY,
    order_item INT NOT NULL,
    order_status INT NOT NULL DEFAULT 0,
    order_num FLOAT(7,2) NOT NULL,
    order_request_date DATE,
    order_purchase_date DATE,
    order_instock_date DATE,

    CONSTRAINT FOREIGN KEY(order_item) REFERENCES items(item_code) ON DELETE CASCADE
    
);
CREATE TABLE usages(
    usage_id INT AUTO_INCREMENT PRIMARY KEY,
    usage_item INT NOT NULL,
    usage_num FLOAT(7,2) NOT NULL,
    usage_date DATE NOT NULL,

    CONSTRAINT FOREIGN KEY(usage_item) REFERENCES items(item_code) ON DELETE CASCADE

);

CREATE TABLE accounts(
    account_id VARCHAR(10) PRIMARY KEY,
    account_name VARCHAR(10) NOT NULL UNIQUE,
    account_passwd VARCHAR(255) NOT NULL,
    account_order BOOLEAN NOT NULL DEFAULT 0,
    account_instock BOOLEAN NOT NULL DEFAULT 0,
    account_item BOOLEAN NOT NULL DEFAULT 0,
    account_management BOOLEAN NOT NULL DEFAULT 0,
    account_session_id VARCHAR(255)
    
);