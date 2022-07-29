# PRIMARY KEY

## Conteúdo

 - [Intro to PRIMARY KEY](#intro)
 - [Creating a PRIMARY KEY](#creating)
 - [Creating PRIMARY KEY with multiple columns](#multiple)
 - [Good practice for primary keys in tables](#good-practices)

---

<div id="intro"></div>

## Intro to PRIMARY KEY

> The SQL **PRIMARY KEY** is a column in a table which must contain a unique value which can be used to identify each and every row of a table uniquely.

**NOTE:**  
Functionally, it is the same as the **UNIQUE constraint**, except that only one **PRIMARY KEY** can be defined for a given table. <u>PRIMARY KEY's will not allow NULL values</u>.

---

<div id="creating"></div>

## Creating a PRIMARY KEY

> Primary keys can be specified at the time of **CREATING TABLE** or the time of changing the structure of the existing table using **ALTER TABLE** statement.

**CREATE TABLE APPROACH:**  
```sql
CREATE TABLE IF NOT EXISTS `table_name` (
  `id` INT NOT NULL,
  //
  //
  PRIMARY KEY (`id`)
);

or

CREATE TABLE IF NOT EXISTS `table_name` (
  `id` INT NOT NULL PRIMARY KEY,
  //
  //
);
```

**ALTER TABLE APPROACH:**  
```sql
ALTER TABLE table_name
ADD PRIMARY KEY (id);
```

---

<div id="multiple"></div>

## Creating PRIMARY KEY with multiple columns

Now, let's see how to create a PRIMARY KEY combining multiple columns:

**CREATE TABLE APPROACH:**  
```sql
CREATE TABLE IF NOT EXISTS `Agents` (
  cust_code char(6) NOT NULL,
  cust_name char(25) NOT  NULL,
  cust_city char(25),
  grade integer,
  agent_code char(6) NOT NULL,
  PRIMARY KEY (`cust_code`, `cust_city`)
);
```

**ALTER TABLE APPROACH:**  
```sql
ALTER TABLE Agents
ADD PRIMARY KEY (`cust_code`, `cust_city`);
```

To testing just enter:

**INPUT:**  
```sql
DESCRIBE Agents;
```

**OUTPUT:**  
```sql
+------------+----------+------+-----+---------+-------+
| Field      | Type     | Null | Key | Default | Extra |
+------------+----------+------+-----+---------+-------+
| cust_code  | char(6)  | NO   | PRI | NULL    |       |
| cust_name  | char(25) | NO   |     | NULL    |       |
| cust_city  | char(25) | NO   | PRI | NULL    |       |
| grade      | int      | YES  |     | NULL    |       |
| agent_code | char(6)  | NO   |     | NULL    |       |
+------------+----------+------+-----+---------+-------+
```

---

<div id="good-practices"></div>

## Good practice for primary keys in tables

 - Primary keys should be as small as necessary. Prefer a numeric type because numeric types are stored in a much more compact format than character formats.
 - Primary keys should never change.
 - Do not use passport number, social security number, or employee contract number as "primary key" as these "primary key" can change for real world situations.

---

**REFERENCES:**  
[SQL PRIMARY KEY Constraint](https://www.w3schools.com/sql/sql_primarykey.ASP)  
[SQL PRIMARY KEY](https://www.w3resource.com/sql/creating-and-maintaining-tables/primary-key.php)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
