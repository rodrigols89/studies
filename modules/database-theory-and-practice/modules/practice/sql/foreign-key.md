# FOREIGN KEY

## Contents

 - [Intro to FOREIGN KEY](#intro)
 - [Creating/Adding FOREIGN KEY relationship to the tables](#relationship)
 - [DROP a FOREIGN KEY Constraint](#drop)

---

<div id="intro"></div>

## Intro to FOREIGN KEY

> The SQL **FOREIGN KEY CONSTRAINT** is used to <u>ensure the referential integrity of the data</u> in one table to match values in another table.

![img](images/CustIdPrimaryKey.gif)  

For example, see tables relation below:

**INPUT:**  
```sql
CREATE TABLE IF NOT EXISTS `Agents` (
  agent_code char(6) NOT NULL,
  agent_name char(25) NOT  NULL,
  PRIMARY KEY (`agent_code`)
);


CREATE TABLE  IF NOT EXISTS `customer` (
  cust_code char(6) NOT NULL,
  cust_name char(25),
  cust_city char(25),
  agent_code char(6),
  PRIMARY KEY (`cust_code`),
  FOREIGN KEY (`agent_code`)
  REFERENCES Agents (`agent_code`)
);
```

![img](images/foreign-key.gif)  

---

<div id="relationship"></div>

## Creating/Adding FOREIGN KEY relationship to the tables

The most common approaches to add **FOREIGN KEY** relationship are:

**CREATE TABLE APPROACH:**  
```sql
CREATE TABLE  IF NOT EXISTS `table_name` (
  //
  //
  FOREIGN KEY(`foreign_key_column_reference_in_current_table`)
  REFERENCES table_reference_with_primary_key (`primary_key_column_in_reference_table`)
);


or


CREATE TABLE  IF NOT EXISTS `table_name` (
  //
  //
  CONSTRAINT `fk_alias_name` FOREIGN KEY (`foreign_key_column_reference_in_current_table`)
  REFERENCES table_reference_with_primary_key (`primary_key_column_in_reference_table`)
);

```

**ALTER TABLE APPROACH:**  
```sql
ALTER TABLE table_name
ADD FOREIGN KEY (`foreign_key_column_reference_in_current_table`)
REFERENCES table_reference_with_primary_key (`primary_key_column_in_reference_table`);


or


ALTER TABLE table_name
ADD CONSTRAINT `fk_alias_name`
FOREIGN KEY (`foreign_key_column_reference_in_current_table`)
REFERENCES table_reference_with_primary_key (`primary_key_column_in_reference_table`);
```

---

<div id="drop"></div>

## DROP a FOREIGN KEY Constraint

To drop a FOREIGN KEY constraint, use the following SQL:

**INPUT:**  
```sql
# MySQL:
ALTER TABLE table_name
DROP FOREIGN KEY fk_alias_name;


or


# SQL Server / Oracle / MS Access:
ALTER TABLE table_name
DROP CONSTRAINT fk_alias_name;
```

---

**REFERENCES:**  
[SQL FOREIGN KEY Constraint](https://www.w3schools.com/sql/sql_foreignkey.asp)  
[SQL FOREIGN KEY](https://www.w3resource.com/sql/creating-and-maintaining-tables/foreign-key.php)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
