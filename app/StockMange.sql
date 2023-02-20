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
    item_descript TEXT,
    item_purchase VARCHAR(255),
);
/*
0 : 구매요청일
1 : 발주일
2 : 입고일
3 : 취소
 */
CREATE TABLE orders(
    order_index INT AUTO_INCREMENT PRIMARY KEY,
    order_item INT NOT NULL,
    order_status INT NOT NULL DEFAULT 0,
    order_num FLOAT(7,2) NOT NULL,
    order_requestdate DATETIME DEFAULT NOW(),
    order_purchasedate DATETIME,
    order_instockdate DATETIME,
    order_canceldate DATETIME,
    

    CONSTRAINT FOREIGN KEY(order_item) REFERENCES items(item_code) ON DELETE CASCADE
    
);

/* CREATE TABLE orderLogs(
    order_log_index INT AUTO_INCREMENT PRIMARY KEY,
    order_type INT NOT NULL,
    order_log_date DATETIME NOT NULL,
    order_log_num FLOAT(7,2) NOT NULL,
    order_log_item INT NOT NULL
    
); */
CREATE TABLE usages(
    usage_id INT AUTO_INCREMENT PRIMARY KEY,
    usage_item INT NOT NULL,
    usage_num FLOAT(7,2) NOT NULL,
    usage_date DATE NOT NULL,
    usage_check BOOLEAN DEFAULT 0,

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
    account_session_id VARCHAR(255) UNIQUE,
    session_expire DATETIME
    
);