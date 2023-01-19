CREATE TABLE `product` (
  prod_code CHAR(6) NOT NULL PRIMARY KEY,
  prod_name CHAR(40),
  com_name CHAR(35),
  life int
);

INSERT INTO product VALUES ('PR001', 'T.V.', 'SONY', 7);
INSERT INTO product VALUES ('PR002', 'DVD PLAYER', 'LG', 9);
INSERT INTO product VALUES ('PR003', 'IPOD', 'PHILIPS', 9);
INSERT INTO product VALUES ('PR004', 'SOUND SYSTEM', 'SONY', 8);
INSERT INTO product VALUES ('PR005', 'MOBILE', 'NOKIA', 6);
