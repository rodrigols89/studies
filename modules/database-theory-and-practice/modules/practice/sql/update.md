# UPDATE

## Contents

 - [Intro to UPDATE statement](#intro)
 - [UPDATE with condition](#condition)
 - [UPDATE multiple columns](#multiple-columns)

---

<div id="intro"></div>

## Intro to UPDATE statement

> Once there is some data in the table, it may be required to modify the data. To do so, the SQL UPDATE command can be used. It changes the records in tables.

 - The SQL UPDATE command changes the data which already exists in the table. Usually, it is needed to make a conditional UPDATE in order to specify which row(s) are going to be updated.
 - The WHERE clause is used to make the update restricted and the updating can happen only on the specified rows.

**NOTE:**  
Without using any WHERE clause (or without making any restriction) the SQL UPDATE command can change all the records for the specific columns of a table.


---

<div id="condition"></div>

## UPDATE with condition

> **WHERE clause** can be used with SQL **UPDATE** to add conditions while modifying records.

For example, to change the value of **'phone_no'** of <u>customer</u> table with **'PHONE NO'** with the following condition:

 1. **'cust_city'** must be **'Torento'**.

The following SQL statement can be used:

**INPUT:**  
```sql
UPDATE customer
SET phone_no='PHONE NO'
WHERE cust_city='Torento';
```

To test:

**INPUT:**  
```sql
SELECT
  phone_no
FROM customer
WHERE
  cust_city='Torento';
```

**OUTPUT:**  
```sql
+----------+
| phone_no |
+----------+
| PHONE NO |
| PHONE NO |
| PHONE NO |
+----------+
```

---

<div id="multiple-columns"></div>

## UPDATE multiple columns

In the following, we are going to discuss how to change the data of more than one columns with the **UPDATE statement**.

For example, to change the value of '**phone_no'** column with **'Phone No'** and **'cust_city'** with **'Kolkata'** and **'grade'** with 1 of <u>customer</u> table with the following condition:

 1. **'agent_code'** must be **'A002'**,

The following SQL statement can be used:

**INPUT:**  
```sql
UPDATE customer
SET
  phone_no='Phone No',
  cust_city='Kolkata',
  grade=1
WHERE
  agent_code='A002';
```

To test:

**INPUT:**  
```sql
SELECT
  phone_no,
  cust_city,
  grade
FROM customer
WHERE
  agent_code='A002';
```

**OUTPUT:**  
```sql
+----------+-----------+-------+
| phone_no | cust_city | grade |
+----------+-----------+-------+
| Phone No | Kolkata   |     1 |
| Phone No | Kolkata   |     1 |
| Phone No | Kolkata   |     1 |
+----------+-----------+-------+
```

---

**REFERENCES:**  
[SQL update with where](https://www.w3resource.com/sql/update-statement/update-with-condition.php)  

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
