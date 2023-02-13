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
    order_index INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL,
    order_item INT NOT NULL,
    order_status INT NOT NULL DEFAULT 0,

    CONSTRAINT FOREIGN KEY(order_item) REFERENCES items(item_code) ON DELETE CASCADE
    
);

CREATE TABLE orderLogs(
    order_log_index INT AUTO_INCREMENT PRIMARY KEY,
    -- order_id와 item_id를 섞어도 unique값이 안된다. -> 상태 로그를 싹 테이블로 나누고 view를 만드는 방법?
    order_log_identifier VARCHAR(50) NOT NULL,
    order_type INT NOT NULL,
    order_log_date DATETIME NOT NULL,
    order_log_num FLOAT(7,2) NOT NULL,

    CONSTRAINT FOREIGN KEY(order_log_identifier) REFERENCES orders(order_identifier) ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY(order_log_item) REFERENCES orders(order_item) ON DELETE CASCADE
    
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
    account_session_id VARCHAR(255) UNIQUE,
    session_expire DATETIME
    
);