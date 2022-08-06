# SELECT

## Contents

 - [Requirements](#requirements)
 - [Selecting all columns](#all)
 - [Using column aliases](#aliases)
 - [SELECT statement with NULL values](#null)
 - [Selecting with distinct](#distinct)
 - [Selecting with DISTINCT on multiple columns](#multiple-columns)

---

<div id="requirements"></div>

## Requirements

Before starting our examples we need create tables and add artificial data to test:

[agents.sql](requirements/agents.sql)
```sql
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
```

[employees.sql](requirements/employees.sql)
```sql
CREATE TABLE IF NOT EXISTS `employees` (
  employee_id INT NOT NULL,
  first_name char(25) NOT NULL,
  last_name char(25) NOT NULL,
  email char(25),
  phone_number char(25) NOT NULL,
  hire_date char(25) NOT NULL,
  job_id char(25) NOT NULL,
  salary DOUBLE NOT NULL,
  manager_id INT NOT NULL,
  department_id INT NOT NULL,
  PRIMARY KEY (`employee_id`)
);


INSERT INTO employees (
  employee_id,
  first_name,
  last_name,
  email,
  phone_number,
  hire_date,
  job_id,
  salary,
  manager_id,
  department_id
)
values
(100, "Steven", "King", NULL, "515.123.4567", "6/17/1987", "AD_PRES", 24000, 100, 90),
(101, "Neena", "Kochhar", "NKOCHHAR", "515.123.4568", "6/18/1987", "AD_VP", 17000, 100, 90),
(102, "Lex", "De Haan", "LDEHAAN", "515.123.4569", "6/19/1987", "AD_VP", 17000, 100, 90),
(103, "Alexander", "Hunold", "AHUNOLD", "590.423.4567", "6/20/1987", "IT_PROG", 9000, 102, 60),
(104, "Bruce", "Ernst", "BERNST", "590.423.4568", "6/21/1987", "IT_PROG", 6000, 103, 60),
(105, "David", "Austin", "DAUSTIN", "590.423.4569", "6/22/1987", "IT_PROG", 4800, 103, 60),
(106, "Valli", "Pataballa", "VPATABAL", "590.423.4560", "6/23/1987", "IT_PROG", 4800, 103, 60),
(107, "Diana", "Lorentz", "DLORENTZ", "590.423.5567", "6/24/1987", "IT_PROG", 4200, 103, 60),
(108, "Nancy", "Greenberg", NULL, "515.124.4569", "6/25/1987", "FI_MGR", 12000, 101, 100),
(109, "Daniel", "Faviet", "DFAVIET", "515.124.4169", "6/26/1987", "FI_ACCOUNT", 9000, 108, 100),
(110, "John", "Chen", "JCHEN", "515.124.4269", "6/27/1987", "FI_ACCOUNT", 8200, 108, 100),
(111, "Ismael", "Sciarra", "ISCIARRA", "515.124.4369", "6/28/1987", "FI_ACCOUNT", 7700, 108, 100),
(112, "Jose Manue", "Urman", "JMURMAN", "515.124.4469", "6/29/1987", "FI_ACCOUNT", 7800, 108, 100),
(113, "Luis", "Popp", "LPOPP", "515.124.4567", "6/30/1987", "FI_ACCOUNT", 6900, 108, 100),
(114, "Den", "Raphaely", "DRAPHEAL", "515.127.4561", "7/1/1987", "PU_MAN", 11000, 100, 30),
(115, "Alexander", "Khoo", "AKHOO", "515.127.4562", "7/2/1987", "PU_CLERK", 3100, 114, 30),
(116, "Shelli", "Baida", "SBAIDA", "515.127.4563", "7/3/1987", "PU_CLERK", 2900, 114, 30),
(117, "Sigal", "Tobias", "STOBIAS", "515.127.4564", "7/4/1987", "PU_CLERK", 2800, 114, 30),
(118, "Guy", "Himuro", "GHIMURO", "515.127.4565", "7/5/1987", "PU_CLERK", 2600, 114, 30),
(119, "Karen", "Colmenares", "KCOLMENA", "515.127.4566", "7/6/1987", "PU_CLERK", 2500, 114, 30),
(120, "Matthew", "Weiss", NULL, "650.123.1234", "7/7/1987", "ST_MAN", 8000, 100, 50),
(121, "Adam", "Fripp", "AFRIPP", "650.123.2234", "7/8/1987", "ST_MAN", 8200, 100, 50),
(122, "Payam", "Kaufling", "PKAUFLIN", "650.123.3234", "7/9/1987", "ST_MAN", 7900, 100, 50),
(123, "Shanta", "Vollman", "SVOLLMAN", "650.123.4234", "7/10/1987", "ST_MAN", 6500, 100, 50),
(124, "Kevin", "Mourgos", "KMOURGOS", "650.123.5234", "7/11/1987", "ST_MAN", 5800, 100, 50),
(125, "Julia", "Nayer", "JNAYER", "650.124.1214", "7/12/1987", "ST_CLERK", 3200, 120, 50),
(126, "Irene", "Mikkilinen", "IMIKKILI", "650.124.1224", "7/13/1987", "ST_CLERK", 2700, 120, 50),
(127, "James", "Landry", "JLANDRY", "650.124.1334", "7/14/1987", "ST_CLERK", 2400, 120, 50),
(128, "Steven", "Markle", "SMARKLE", "650.124.1434", "7/15/1987", "ST_CLERK", 2200, 120, 50),
(129, "Laura", "Bissot", "LBISSOT", "650.124.5234", "7/16/1987", "ST_CLERK", 3300, 121, 50),
(130, "Mozhe", "Atkinson", "MATKINSO", "650.124.6234", "7/17/1987", "ST_CLERK", 2800, 121, 50),
(131, "James", "Marlow", "JAMRLOW", "650.124.7234", "7/18/1987", "ST_CLERK", 2500, 121, 50),
(132, "TJ", "Olson", "TJOLSON", "650.124.8234", "7/19/1987", "ST_CLERK", 2100, 121, 50),
(133, "Jason", "Mallin", "JMALLIN", "650.127.1934", "7/20/1987", "ST_CLERK", 3300, 122, 50),
(134, "Michael", "Rogers", "MROGERS", "650.127.1834", "7/21/1987", "ST_CLERK", 2900, 122, 50),
(135, "Ki", "Gee", "KGEE", "650.127.1734", "7/22/1987", "ST_CLERK", 2400, 122, 50),
(136, "Hazel", "Philtanker", "HPHILTAN", "650.127.1634", "7/23/1987", "ST_CLERK", 2200, 122, 50),
(137, "Renske", "Ladwig", "RLADWIG", "650.121.1234", "7/24/1987", "ST_CLERK", 3600, 123, 50),
(138, "Stephen", "Stiles", "SSTILES", "650.121.2034", "7/25/1987", "ST_CLERK", 3200, 123, 50),
(139, "John", "Seo", "JSEO", "650.121.2019", "7/26/1987", "ST_CLERK", 2700, 123, 50),
(140, "Joshua", "Patel", "JPATEL", "650.121.1834", "7/27/1987", "ST_CLERK", 2500, 123, 50),
(141, "Trenna", "Rajs", "TRAJS", "650.121.8009", "7/28/1987", "ST_CLERK", 3500, 124, 50),
(142, "Curtis", "Davies", "CDAVIES", "650.121.2994", "7/29/1987", "ST_CLERK", 3100, 124, 50),
(143, "Randall", "Matos", "RMATOS", "650.121.2874", "7/30/1987", "ST_CLERK", 2600, 124, 50),
(144, "Peter", "Vargas", NULL, "650.121.2004", "7/31/1987", "ST_CLERK", 2500, 124, 50),
(145, "John", "Russell", "JRUSSEL", "011.44.1344.", "8/1/1987", "SA_MAN", 14000, 100, 80),
(146, "Karen", "Partners", "KPARTNER", "011.44.1344.", "8/2/1987", "SA_MAN", 13500, 100, 80),
(147, "Alberto", "Errazuriz", "AERRAZUR", "011.44.1344.", "8/3/1987", "SA_MAN", 12000, 100, 80),
(148, "Gerald", "Cambrault", "GCAMBRAU", "011.44.1344.", "8/4/1987", "SA_MAN", 11000, 100, 80),
(149, "Eleni", "Zlotkey", NULL, "011.44.1344.", "8/5/1987", "SA_MAN", 10500, 100, 80),
(150, "Peter", "Tucker", NULL, "011.44.1344.", "8/6/1987", "SA_REP", 10000, 145, 80),
(151, "David", "Bernstein", NULL, "011.44.1344.", "8/7/1987", "SA_REP", 9500, 145, 80),
(152, "Peter", "Hall", "PHALL", "011.44.1344.", "8/8/1987", "SA_REP", 9000, 145, 80),
(153, "Christophe", "Olsen", "COLSEN", "011.44.1344.", "8/9/1987", "SA_REP", 8000, 145, 80),
(154, "Nanette", "Cambrault", "NCAMBRAU", "011.44.1344.", "8/10/1987", "SA_REP", 7500, 145, 80),
(155, "Oliver", "Tuvault", "OTUVAULT", "011.44.1344.", "8/11/1987", "SA_REP", 7000, 145, 80),
(156, "Janette", "King", "JKING", "011.44.1345.", "8/12/1987", "SA_REP", 10000, 146, 80),
(157, "Patrick", "Sully", "PSULLY", "011.44.1345.", "8/13/1987", "SA_REP", 9500, 146, 80),
(158, "Allan", "McEwen", "AMCEWEN", "011.44.1345.", "8/14/1987", "SA_REP", 9000, 146, 80),
(159, "Lindsey", "Smith", "LSMITH", "011.44.1345.", "8/15/1987", "SA_REP", 8000, 146, 80),
(160, "Louise", "Doran", "LDORAN", "011.44.1345.", "8/16/1987", "SA_REP", 7500, 146, 80),
(161, "Sarath", "Sewall", "SSEWALL", "011.44.1345.", "8/17/1987", "SA_REP", 7000, 146, 80),
(162, "Clara", "Vishney", "CVISHNEY", "011.44.1346.", "8/18/1987", "SA_REP", 10500, 147, 80),
(163, "Danielle", "Greene", "DGREENE", "011.44.1346.", "8/19/1987", "SA_REP", 9500, 147, 80),
(164, "Mattea", "Marvins", "MMARVINS", "011.44.1346.", "8/20/1987", "SA_REP", 7200, 147, 80),
(165, "David", "Lee", "DLEE", "011.44.1346.", "8/21/1987", "SA_REP", 6800, 147, 80),
(166, "Sundar", "Ande", "SANDE", "011.44.1346.", "8/22/1987", "SA_REP", 6400, 147, 80),
(167, "Amit", "Banda", "ABANDA", "011.44.1346.", "8/23/1987", "SA_REP", 6200, 147, 80),
(168, "Lisa", "Ozer", "LOZER", "011.44.1343.", "8/24/1987", "SA_REP", 11500, 148, 80),
(169, "Harrison", "Bloom", "HBLOOM", "011.44.1343.", "8/25/1987", "SA_REP", 10000, 148, 80),
(170, "Tayler", "Fox", "TFOX", "011.44.1343.", "8/26/1987", "SA_REP", 9600, 148, 80),
(171, "William", "Smith", "WSMITH", "011.44.1343.", "8/27/1987", "SA_REP", 7400, 148, 80),
(172, "Elizabeth", "Bates", "EBATES", "011.44.1343.", "8/28/1987", "SA_REP", 7300, 148, 80),
(173, "Sundita", "Kumar", "SKUMAR", "011.44.1343.", "8/29/1987", "SA_REP", 6100, 148, 80),
(174, "Ellen", "Abel", "EABEL", "011.44.1644.", "8/30/1987", "SA_REP", 11000, 149, 80),
(175, "Alyssa", "Hutton", "AHUTTON", "011.44.1644.", "8/31/1987", "SA_REP", 8800, 149, 80),
(176, "Jonathon", "Taylor", "JTAYLOR", "011.44.1644.", "9/1/1987", "SA_REP", 8600, 149, 80),
(177, "Jack", "Livingston", "JLIVINGS", "011.44.1644.", "9/2/1987", "SA_REP", 8400, 149, 80),
(178, "Kimberely", "Grant", "KGRANT", "011.44.1644.", "9/3/1987", "SA_REP", 7000, 149, 80),
(179, "Charles", "Johnson", "CJOHNSON", "011.44.1644.", "9/4/1987", "SA_REP", 6200, 149, 80),
(180, "Winston", "Taylor", "WTAYLOR", "650.507.9876", "9/5/1987", "SH_CLERK", 3200, 120, 50),
(181, "Jean", "Fleaur", "JFLEAUR", "650.507.9877", "9/6/1987", "SH_CLERK", 3100, 120, 50),
(182, "Martha", "Sullivan", "MSULLIVA", "650.507.9878", "9/7/1987", "SH_CLERK", 2500, 120, 50),
(183, "Girard", "Geoni", "GGEONI", "650.507.9879", "9/8/1987", "SH_CLERK", 2800, 120, 50),
(184, "Nandita", "Sarchand", "NSARCHAN", "650.509.1876", "9/9/1987", "SH_CLERK", 4200, 121, 50),
(185, "Alexis", "Bull", "ABULL", "650.509.2876", "9/10/1987", "SH_CLERK", 4100, 121, 50),
(186, "Julia", "Dellinger", "JDELLING", "650.509.3876", "9/11/1987", "SH_CLERK", 3400, 121, 50),
(187, "Anthony", "Cabrio", "ACABRIO", "650.509.4876", "9/12/1987", "SH_CLERK", 3000, 121, 50),
(188, "Kelly", "Chung", "KCHUNG", "650.505.1876", "9/13/1987", "SH_CLERK", 3800, 122, 50),
(189, "Jennifer", "Dilly", "JDILLY", "650.505.2876", "9/14/1987", "SH_CLERK", 3600, 122, 50),
(190, "Timothy", "Gates", "TGATES", "650.505.3876", "9/15/1987", "SH_CLERK", 2900, 122, 50),
(191, "Randall", "Perkins", "RPERKINS", "650.505.4876", "9/16/1987", "SH_CLERK", 2500, 122, 50),
(192, "Sarah", "Bell", "SBELL", "650.501.1876", "9/17/1987", "SH_CLERK", 4000, 123, 50),
(193, "Britney", "Everett", "BEVERETT", "650.501.2876", "9/18/1987", "SH_CLERK", 3900, 123, 50),
(194, "Samuel", "McCain", "SMCCAIN", "650.501.3876", "9/19/1987", "SH_CLERK", 3200, 123, 50),
(195, "Vance", "Jones", "VJONES", "650.501.4876", "9/20/1987", "SH_CLERK", 2800, 123, 50),
(196, "Alana", "Walsh", "AWALSH", "650.507.9811", "9/21/1987", "SH_CLERK", 3100, 124, 50),
(197, "Kevin", "Feeney", "KFEENEY", "650.507.9822", "9/22/1987", "SH_CLERK", 3000, 124, 50),
(198, "Donald", "OConnell", "DOCONNEL", "650.507.9833", "9/23/1987", "SH_CLERK", 2600, 124, 50),
(199, "Douglas", "Grant", "DGRANT", "650.507.9844", "9/24/1987", "SH_CLERK", 2600, 124, 50),
(200, "Jennifer", "Whalen", "JWHALEN", "515.123.4444", "9/25/1987", "AD_ASST", 4400, 101, 10),
(201, "Michael", "Hartstein", "MHARTSTE", "515.123.5555", "9/26/1987", "MK_MAN", 13000, 100, 20),
(202, "Pat", "Fay", "PFAY", "603.123.6666", "9/27/1987", "MK_REP", 6000, 201, 20),
(203, "Susan","Mavris", "SMAVRIS", "515.123.7777", "9/28/1987", "HR_REP", 6500, 101, 40),
(204, "Hermann", "Baer", "HBAER", "515.123.8888", "9/29/1987", "PR_REP", 10000, 101, 70),
(205, "Shelley", "Higgins", "SHIGGINS", "515.123.8080", "9/30/1987", "AC_MGR", 12000, 101, 110),
(206, "William", "Gietz", "WGIETZ", "515.123.8181 ", "10/1/1987", "AC_ACCOUNT", 8300, 205, 110);
```

---

<div id="all"></div>

## Selecting all columns

> To retrieve all the columns from a table, `*` character is used with SQL SELECT statement.

For example, the following query displays all the columns of agents table:

**INPUT:**  
```sql
SELECT * FROM agents;
```

**OUTPUT:**  
```sql
+------------+------------+---------------+-----------+--------------+----------------+
| agent_code | agent_name | working_area  | comission | phone_no     | country        |
+------------+------------+---------------+-----------+--------------+----------------+
| A001       | Anderson   | Bangalore     | 0.11      | 045-21447739 | France         |
| A002       | Subbarao   | Mumbai        | 0.15      | 077-12346674 | United States  |
| A003       | Alex       | London        | 0.12      | 075-12458969 | United States  |
| A004       | McDen      | Torento       | 0.11      | 078-22255588 | Russian        |
| A005       | Lucida     | Brisban       | 0.14      | 044-52981425 | United Kingdom |
| A006       | Mukesh     | London        | 0.15      | 029-12358964 | Brazil         |
| A007       | Ramasundar | Bangalore     | 0.15      | 077-25814763 | Brazil         |
| A008       | Alford     | New York      | 0.15      | 044-25874365 | United States  |
| A009       | Ivan       | Hampshair     | 0.13      | 008-22544166 | United Kingdom |
| A010       | Kumar      | Chennai       | 0.12      | 007-22388644 | Germany        |
| A011       | Ravi       | Bangalore     | 0.14      | 077-45625874 | Brazil         |
| A012       | Santakumar | San Jose      | 0.13      | 007-11118644 | United Kingdom |
| A024       | Mary       | San Francisco | 0.15      | 008-22511000 | United States  |
| A030       | Benjamin   | Seattle       | 0.12      | 008-22536178 | Russian        |
| A055       | Margot     | Boston        | 0.12      | 008-22532200 | United States  |
+------------+------------+---------------+-----------+--------------+----------------+
15 rows in set (0.00 sec)
```

This's equivalent to:

**INPUT:**  
```sql
SELECT agent_code, agent_name, working_area,
commission, phone_no, country
FROM agents;
```

**OUTPUT:**  
```sql
+------------+------------+---------------+------------+--------------+----------------+
| agent_code | agent_name | working_area  | commission | phone_no     | country        |
+------------+------------+---------------+------------+--------------+----------------+
| A001       | Anderson   | Bangalore     | 0.11       | 045-21447739 | France         |
| A002       | Subbarao   | Mumbai        | 0.15       | 077-12346674 | United States  |
| A003       | Alex       | London        | 0.12       | 075-12458969 | United States  |
| A004       | McDen      | Torento       | 0.11       | 078-22255588 | Russian        |
| A005       | Lucida     | Brisban       | 0.14       | 044-52981425 | United Kingdom |
| A006       | Mukesh     | London        | 0.15       | 029-12358964 | Brazil         |
| A007       | Ramasundar | Bangalore     | 0.15       | 077-25814763 | Brazil         |
| A008       | Alford     | New York      | 0.15       | 044-25874365 | United States  |
| A009       | Ivan       | Hampshair     | 0.13       | 008-22544166 | United Kingdom |
| A010       | Kumar      | Chennai       | 0.12       | 007-22388644 | Germany        |
| A011       | Ravi       | Bangalore     | 0.14       | 077-45625874 | Brazil         |
| A012       | Santakumar | San Jose      | 0.13       | 007-11118644 | United Kingdom |
| A024       | Mary       | San Francisco | 0.15       | 008-22511000 | United States  |
| A030       | Benjamin   | Seattle       | 0.12       | 008-22536178 | Russian        |
| A055       | Margot     | Boston        | 0.12       | 008-22532200 | United States  |
+------------+------------+---------------+------------+--------------+----------------+
```

---

<div id="aliases"></div>

## Using column aliases

 - To renames a column heading temporarily for a particular SQL query you can use column aliases.
 - There can be an optional AS keyword between the column name and alias
 - It requires double quotation marks if the column name string contains spaces or special characters or if it is case sensitive.

See the following examples using AS keyword and without AS Keyword.

**WITH "AS" KEYWORD:**  
```sql
SELECT first_name AS "First Name", 
last_name AS "Last Name", salary AS "Salary"
FROM employees;
```

**WITHOUT "AS" KEYWORD:**  
```sql
SELECT first_name "First Name", 
last_name "Last Name", salary "Salary"
FROM employees;
```

**OUTPUT:**  
```cli
+------------+------------+--------+
| First Name | Last Name  | Salary |
+------------+------------+--------+
| Steven     | King       |  24000 |
| Neena      | Kochhar    |  17000 |
| Lex        | De Haan    |  17000 |
| Alexander  | Hunold     |   9000 |
| Bruce      | Ernst      |   6000 |
| David      | Austin     |   4800 |
| Valli      | Pataballa  |   4800 |
| Diana      | Lorentz    |   4200 |
| Nancy      | Greenberg  |  12000 |
| Daniel     | Faviet     |   9000 |
| John       | Chen       |   8200 |
| Ismael     | Sciarra    |   7700 |
| Jose Manue | Urman      |   7800 |
| Luis       | Popp       |   6900 |
| Den        | Raphaely   |  11000 |
| Alexander  | Khoo       |   3100 |
| Shelli     | Baida      |   2900 |
| Sigal      | Tobias     |   2800 |
| Guy        | Himuro     |   2600 |
| Karen      | Colmenares |   2500 |
| Matthew    | Weiss      |   8000 |
| Adam       | Fripp      |   8200 |
| Payam      | Kaufling   |   7900 |
| Shanta     | Vollman    |   6500 |
| Kevin      | Mourgos    |   5800 |
| Julia      | Nayer      |   3200 |
| Irene      | Mikkilinen |   2700 |
| James      | Landry     |   2400 |
| Steven     | Markle     |   2200 |
| Laura      | Bissot     |   3300 |
| Mozhe      | Atkinson   |   2800 |
| James      | Marlow     |   2500 |
| TJ         | Olson      |   2100 |
| Jason      | Mallin     |   3300 |
| Michael    | Rogers     |   2900 |
| Ki         | Gee        |   2400 |
| Hazel      | Philtanker |   2200 |
| Renske     | Ladwig     |   3600 |
| Stephen    | Stiles     |   3200 |
| John       | Seo        |   2700 |
| Joshua     | Patel      |   2500 |
| Trenna     | Rajs       |   3500 |
| Curtis     | Davies     |   3100 |
| Randall    | Matos      |   2600 |
| Peter      | Vargas     |   2500 |
| John       | Russell    |  14000 |
| Karen      | Partners   |  13500 |
| Alberto    | Errazuriz  |  12000 |
| Gerald     | Cambrault  |  11000 |
| Eleni      | Zlotkey    |  10500 |
| Peter      | Tucker     |  10000 |
| David      | Bernstein  |   9500 |
| Peter      | Hall       |   9000 |
| Christophe | Olsen      |   8000 |
| Nanette    | Cambrault  |   7500 |
| Oliver     | Tuvault    |   7000 |
| Janette    | King       |  10000 |
| Patrick    | Sully      |   9500 |
| Allan      | McEwen     |   9000 |
| Lindsey    | Smith      |   8000 |
| Louise     | Doran      |   7500 |
| Sarath     | Sewall     |   7000 |
| Clara      | Vishney    |  10500 |
| Danielle   | Greene     |   9500 |
| Mattea     | Marvins    |   7200 |
| David      | Lee        |   6800 |
| Sundar     | Ande       |   6400 |
| Amit       | Banda      |   6200 |
| Lisa       | Ozer       |  11500 |
| Harrison   | Bloom      |  10000 |
| Tayler     | Fox        |   9600 |
| William    | Smith      |   7400 |
| Elizabeth  | Bates      |   7300 |
| Sundita    | Kumar      |   6100 |
| Ellen      | Abel       |  11000 |
| Alyssa     | Hutton     |   8800 |
| Jonathon   | Taylor     |   8600 |
| Jack       | Livingston |   8400 |
| Kimberely  | Grant      |   7000 |
| Charles    | Johnson    |   6200 |
| Winston    | Taylor     |   3200 |
| Jean       | Fleaur     |   3100 |
| Martha     | Sullivan   |   2500 |
| Girard     | Geoni      |   2800 |
| Nandita    | Sarchand   |   4200 |
| Alexis     | Bull       |   4100 |
| Julia      | Dellinger  |   3400 |
| Anthony    | Cabrio     |   3000 |
| Kelly      | Chung      |   3800 |
| Jennifer   | Dilly      |   3600 |
| Timothy    | Gates      |   2900 |
| Randall    | Perkins    |   2500 |
| Sarah      | Bell       |   4000 |
| Britney    | Everett    |   3900 |
| Samuel     | McCain     |   3200 |
| Vance      | Jones      |   2800 |
| Alana      | Walsh      |   3100 |
| Kevin      | Feeney     |   3000 |
| Donald     | OConnell   |   2600 |
| Douglas    | Grant      |   2600 |
| Jennifer   | Whalen     |   4400 |
| Michael    | Hartstein  |  13000 |
| Pat        | Fay        |   6000 |
| Susan      | Mavris     |   6500 |
| Hermann    | Baer       |  10000 |
| Shelley    | Higgins    |  12000 |
| William    | Gietz      |   8300 |
+------------+------------+--------+
```

---

<div id="null"></div>

## SELECT statement with NULL values

Before storing a value in any field of a table, a NULL value can be stored; later that NULL value can be replaced with the desired value. When a field value is NULL it means that the database assigned nothing `(not even a zero "0" or blank " " )`, in that field for that row.

For example, let's see examples with email is NULL:

**INPUT:**  
```sql
SELECT * FROM employees
WHERE email IS NULL;
```

**OUTPUT:**  
```sql
+-------------+------------+-----------+-------+--------------+-----------+----------+--------+------------+---------------+
| employee_id | first_name | last_name | email | phone_number | hire_date | job_id   | salary | manager_id | department_id |
+-------------+------------+-----------+-------+--------------+-----------+----------+--------+------------+---------------+
|         100 | Steven     | King      | NULL  | 515.123.4567 | 6/17/1987 | AD_PRES  |  24000 |        100 |            90 |
|         108 | Nancy      | Greenberg | NULL  | 515.124.4569 | 6/25/1987 | FI_MGR   |  12000 |        101 |           100 |
|         120 | Matthew    | Weiss     | NULL  | 650.123.1234 | 7/7/1987  | ST_MAN   |   8000 |        100 |            50 |
|         144 | Peter      | Vargas    | NULL  | 650.121.2004 | 7/31/1987 | ST_CLERK |   2500 |        124 |            50 |
|         149 | Eleni      | Zlotkey   | NULL  | 011.44.1344. | 8/5/1987  | SA_MAN   |  10500 |        100 |            80 |
|         150 | Peter      | Tucker    | NULL  | 011.44.1344. | 8/6/1987  | SA_REP   |  10000 |        145 |            80 |
|         151 | David      | Bernstein | NULL  | 011.44.1344. | 8/7/1987  | SA_REP   |   9500 |        145 |            80 |
+-------------+------------+-----------+-------+--------------+-----------+----------+--------+------------+---------------+
```

---

<div id="distinct"></div>

## Selecting with distinct

Redundancy is the repetition of certain data in a table. With the use of **DISTINCT** clause data redundancy may be avoided. This clause will eliminate the repetitive appearance of same data.

**NOTE:**  
**DISTINCT** can come only once in a given select statement.

**Syntax:**
```sql
SELECT DISTINCT <column_name> 
FROM <table_name> 
WHERE <conditions>;
```

**Pictorial presentation:**  
![img](images/sql-distinct.png)  

**INPUT:**  
```sql
SELECT DISTINCT working_area
FROM agents
ORDER BY working_area;
```

**OUTPUT:**  
```sql
+---------------+
| working_area  |
+---------------+
| Bangalore     |
| Boston        |
| Brisban       |
| Chennai       |
| Hampshair     |
| London        |
| Mumbai        |
| New York      |
| San Francisco |
| San Jose      |
| Seattle       |
| Torento       |
+---------------+
```

---

<div id="multiple-columns"></div>

## SQL SELECT with DISTINCT on multiple columns

Now, let's see <u>SELECT with DISTINCT on multiple columns</u> examples:

**Two columns examples:**  
![img](images/distinct1.png)  

---

![img](images/distinct2.png)  

---

![img](images/distinct5.png)  

---

**Three columns examples:**  
![img](images/distinct3.png)  

---

![img](images/distinct4.png)  

---

![img](images/distinct6.png)  

---

**REFERENCES:**  
[SQL SELECT statement](https://www.w3resource.com/sql/select-statement/sql-select-statement.php)  
[SQL DISTINCT](https://www.w3resource.com/sql/select-statement/queries-with-distinct.php)  
[SQL SELECT with DISTINCT on multiple columns](https://www.w3resource.com/sql/select-statement/queries-with-distinct-multiple-columns.php)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**