CREATE TABLE IF NOT EXISTS `agents` (
  agent_code char(6) NOT NULL,
  agent_name char(25) NOT NULL,
  working_area char(25) NOT NULL,
  commission char(6) NOT NULL,
  phone_no char(25),
  country char(25),
  PRIMARY KEY (`agent_code`)
);

INSERT INTO agents (agent_code, agent_name, working_area, commission, phone_no, country)
values
('A007', 'Ramasundar', 'Bangalore', '0.15', '077-25814763', 'Brazil'),
('A003', 'Alex', 'London', '0.12', '075-12458969', 'United States'),
('A008', 'Alford', 'New York', '0.15', '044-25874365', 'United States'),
('A011', 'Ravi', 'Bangalore', '0.14', '077-45625874', 'Brazil'),
('A010', 'Kumar', 'Chennai', '0.12', '007-22388644', 'Germany'),
('A012', 'Santakumar', 'San Jose', '0.13', '007-11118644', 'United Kingdom'),
('A005', 'Lucida', 'Brisban', '0.14', '044-52981425', 'United Kingdom'),
('A001', 'Anderson', 'Bangalore', '0.11', '045-21447739', 'France'),
('A002', 'Subbarao', 'Mumbai', '0.15', '077-12346674', 'United States'),
('A006', 'Mukesh', 'London', '0.15', '029-12358964', 'Brazil'),
('A004', 'McDen', 'Torento', '0.11', '078-22255588', 'Russian'),
('A009', 'Ivan', 'Hampshair', '0.13', '008-22544166', 'United Kingdom'),
('A030', 'Benjamin', 'Seattle', '0.12', '008-22536178', 'Russian'),
('A055', 'Margot', 'Boston', '0.12', '008-22532200', 'United States'),
('A024', 'Mary', 'San Francisco', '0.15', '008-22511000', 'United States');
