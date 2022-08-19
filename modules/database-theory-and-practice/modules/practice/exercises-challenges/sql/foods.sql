CREATE TABLE IF NOT EXISTS `foods` (
  item_id INT NOT NULL PRIMARY KEY,
  item_name VARCHAR(40) NOT NULL,
  item_unit VARCHAR(40),
  company_id INT REFERENCES company
);

INSERT INTO foods VALUES (1, 'Chex Mix', 'Pcs', 16);
INSERT INTO foods VALUES (6, 'Cheez-It', 'Pcs', 15);
INSERT INTO foods VALUES (2, 'BN Biscuit', 'Pcs', 15);
INSERT INTO foods VALUES (3, 'Mighty Munch', 'Pcs', 17);
INSERT INTO foods VALUES (4, 'Pot Rice', 'Pcs', 15);
INSERT INTO foods VALUES (5, 'Jaffa Cakes', 'Pcs', 18);
INSERT INTO foods VALUES (7, 'Salt n Shake', 'Pcs', NULL);
