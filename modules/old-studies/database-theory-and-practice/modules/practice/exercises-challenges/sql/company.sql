CREATE TABLE IF NOT EXISTS `company` (
  company_id INT NOT NULL PRIMARY KEY,
  company_name VARCHAR(40) NOT NULL,
  company_city VARCHAR(40)
);

INSERT INTO company VALUES (18, 'Order All', 'Boston');
INSERT INTO company VALUES (15, 'Jack Hill Ltd', 'London');
INSERT INTO company VALUES (16, 'Akas Foods', 'Delhi');
INSERT INTO company VALUES (17, 'Foodies', 'London');
INSERT INTO company VALUES (19, 'sip-n-Bite', 'New York');
