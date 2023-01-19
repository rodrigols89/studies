CREATE TABLE `purchase` (
  pur_no CHAR(6) NOT NULL PRIMARY KEY,
  prod_code CHAR(40) NOT NULL REFERENCES product,
  prod_name CHAR(35) NOT NULL REFERENCES product,
  com_name CHAR(35) NOT NULL REFERENCES product,
  pur_qty CHAR(35),
  pur_amount CHAR(35)
);

INSERT INTO purchase VALUES (2, 'PR001', 'T.V.', 'SONY', 15, 450000);
INSERT INTO purchase VALUES (1, 'PR003', 'IPOD', 'PHILIPS', 20, 60000);
INSERT INTO purchase VALUES (3, 'PR007', 'LAPTOP', 'H.P.', 6, 240000);
INSERT INTO purchase VALUES (4, 'PR005', 'MOBILE', 'NOKIA', 100, 300000);
INSERT INTO purchase VALUES (5, 'PR002', 'DVD PLAYER', 'LG', 10, 30000);
INSERT INTO purchase VALUES (6, 'PR006', 'SOUND SYSTEM', 'CREATIVE', 8, 40000);
