# JOIN

## Contents

<div id=""></div>

 - **introductions:**
   - [JOIN clause](#intro)
   - ["Equi" (=) JOIN](#equi-join)
   - ["Non" Equi (>, <, >=, <=) JOIN](#no-equi)
   - [INNER JOIN](#inner-join)
   - [NATURAL JOIN](#natural-join)
   - [CROSS JOIN](#cross-join)
   - [OUTER JOIN](#outer-join)
   - [LEFT JOIN](#left-join)
   - [RIGHT JOIN](#right-join)
   - [FULL OUTER JOIN](#full-outer-join)
 - **Tips & Tricks:**
   - [Difference between "NATURAL JOIN" and "INNER JOIN"](#nj-ij)
   - [Difference between "JOIN" and "INNER JOIN"](#join-vs-inner-join)
   - [Difference between WHERE and ON in SQL](#on-where)
   - [JOIN and Veen Diagrams](#diagrams)
 - **Examples:**
   - [Coming soon...](#)

---

<div id="intro"></div>

## JOIN clause

> An SQL JOIN clause combines rows from two or more tables. It creates a set of rows in a temporary table.

**NOTE:**  
A JOIN works on two or more tables if they have at least one common field and <u>have a relationship between them</u>.

For example, see image below:

![img](images/sql-joins-all.gif)  

For example, imagine you have the follows tables:

[company.sql](../exercises-challenges/sql/company.sql)
```sql
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
```

[foods.sql](../exercises-challenges/sql/foods.sql)
```sql
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
```

To join two tables **'company'** and **'foods'**, the following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    company.company_id, company.company_name,
    foods.item_id, foods.item_name
FROM
    company, foods;
```

**OUTPUT:**  
```SQL
+------------+---------------+---------+--------------+
| company_id | company_name  | item_id | item_name    |
+------------+---------------+---------+--------------+
|         19 | sip-n-Bite    |       1 | Chex Mix     |
|         18 | Order All     |       1 | Chex Mix     |
|         17 | Foodies       |       1 | Chex Mix     |
|         16 | Akas Foods    |       1 | Chex Mix     |
|         15 | Jack Hill Ltd |       1 | Chex Mix     |
|         19 | sip-n-Bite    |       2 | BN Biscuit   |
|         18 | Order All     |       2 | BN Biscuit   |
|         17 | Foodies       |       2 | BN Biscuit   |
|         16 | Akas Foods    |       2 | BN Biscuit   |
|         15 | Jack Hill Ltd |       2 | BN Biscuit   |
|         19 | sip-n-Bite    |       3 | Mighty Munch |
|         18 | Order All     |       3 | Mighty Munch |
|         17 | Foodies       |       3 | Mighty Munch |
|         16 | Akas Foods    |       3 | Mighty Munch |
|         15 | Jack Hill Ltd |       3 | Mighty Munch |
|         19 | sip-n-Bite    |       4 | Pot Rice     |
|         18 | Order All     |       4 | Pot Rice     |
|         17 | Foodies       |       4 | Pot Rice     |
|         16 | Akas Foods    |       4 | Pot Rice     |
|         15 | Jack Hill Ltd |       4 | Pot Rice     |
|         19 | sip-n-Bite    |       5 | Jaffa Cakes  |
|         18 | Order All     |       5 | Jaffa Cakes  |
|         17 | Foodies       |       5 | Jaffa Cakes  |
|         16 | Akas Foods    |       5 | Jaffa Cakes  |
|         15 | Jack Hill Ltd |       5 | Jaffa Cakes  |
|         19 | sip-n-Bite    |       6 | Cheez-It     |
|         18 | Order All     |       6 | Cheez-It     |
|         17 | Foodies       |       6 | Cheez-It     |
|         16 | Akas Foods    |       6 | Cheez-It     |
|         15 | Jack Hill Ltd |       6 | Cheez-It     |
|         19 | sip-n-Bite    |       7 | Salt n Shake |
|         18 | Order All     |       7 | Salt n Shake |
|         17 | Foodies       |       7 | Salt n Shake |
|         16 | Akas Foods    |       7 | Salt n Shake |
|         15 | Jack Hill Ltd |       7 | Salt n Shake |
+------------+---------------+---------+--------------+
```

---

<div id="equi-join"></div>

## "Equi" (=) JOIN

> SQL EQUI JOIN performs a JOIN against <u>equality</u> or <u>matching</u> column(s) values of the associated tables.

**NOTE:**  
An equal sign (=) is used as comparison operator in the where clause to refer equality.

For example, see image below:

![img](images/sql-equi-join-image.gif)  

**NOTE:**  
See that **"Equi Join"** <u>excludes different values</u> from the **SELECT** statement.

---

<div id="no-equi"></div>

## "Non" Equi (>, <, >=, <=) JOIN

> The SQL **NON EQUI JOIN** uses <u>comparison operator</u> instead of the equal sign like **>, <, >=, <=** along with conditions.

**Pictorial presentation of SQL Non Equi Join:**  
![img](images/sql-non-equi-join-image.gif)  

Another example is the following:

**INPUT:**  
```sql
SELECT
    a.ord_num, a.ord_amount,
    b.cust_name, b.working_area
FROM
    orders a, customer b
WHERE
    a.ord_amount BETWEEN b.opening_amt AND b.opening_amt;
```

**OUTPUT:**  
```sql
+---------+------------+-----------+--------------+
| ord_num | ord_amount | cust_name | working_area |
+---------+------------+-----------+--------------+
|  200101 |       3000 | Micheal   | New York     |
|  200108 |       4000 | Cook      | London       |
|  200108 |       4000 | Karl      | London       |
|  200110 |       3000 | Micheal   | New York     |
|  200113 |       4000 | Cook      | London       |
|  200113 |       4000 | Karl      | London       |
|  200119 |       4000 | Cook      | London       |
|  200119 |       4000 | Karl      | London       |
+---------+------------+-----------+--------------+
```

---

<div id="inner-join"></div>

## INNER JOIN

The INNER JOIN selects all rows from both participating tables as long as there is a match between the columns. An SQL INNER JOIN is same as JOIN clause, combining rows from two or more tables.

**Pictorial presentation of SQL Inner Join:**  
![img](images/sql-inner-jon.gif)  

**NOTE:**  
The INNER JOIN in SQL joins two tables according to the matching of a certain criteria using a comparison operator.

For example, to join **item_name**, item_unit columns from <u>foods</u> table and **company_name**, company_city columns from <u>company</u> table, with the following condition:

 1. company_id of foods and company table must be same.

The following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    foods.item_name, foods.item_unit,
    company.company_name, company.company_city
FROM foods INNER JOIN company
ON
    foods.company_id=company.company_id;
```

**OUTPUT:**  
```sql
+--------------+-----------+---------------+--------------+
| item_name    | item_unit | company_name  | company_city |
+--------------+-----------+---------------+--------------+
| Chex Mix     | Pcs       | Akas Foods    | Delhi        |
| BN Biscuit   | Pcs       | Jack Hill Ltd | London       |
| Mighty Munch | Pcs       | Foodies       | London       |
| Pot Rice     | Pcs       | Jack Hill Ltd | London       |
| Jaffa Cakes  | Pcs       | Order All     | Boston       |
| Cheez-It     | Pcs       | Jack Hill Ltd | London       |
+--------------+-----------+---------------+--------------+
```

**Example of SQL INNER JOIN using JOIN keyword:**  
To get **item_name**, item_unit columns from <u>foods</u> table and **company_name**, **company_city** columns from <u>company</u> table, after joining these mentioned tables, with the following condition:

 1. company id of foods and company id of company table must be same.

The following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    foods.item_name, foods.item_unit,
    company.company_name, company.company_city
FROM foods JOIN company
ON
    foods.company_id=company.company_id;
```

**OUTPUT:**  
```sql
+--------------+-----------+---------------+--------------+
| item_name    | item_unit | company_name  | company_city |
+--------------+-----------+---------------+--------------+
| Chex Mix     | Pcs       | Akas Foods    | Delhi        |
| BN Biscuit   | Pcs       | Jack Hill Ltd | London       |
| Mighty Munch | Pcs       | Foodies       | London       |
| Pot Rice     | Pcs       | Jack Hill Ltd | London       |
| Jaffa Cakes  | Pcs       | Order All     | Boston       |
| Cheez-It     | Pcs       | Jack Hill Ltd | London       |
+--------------+-----------+---------------+--------------+
```

**Pictorial Presentation of SQL Inner Join of Company and Foods Tables:**  
![img](images/sql-inner-join-set-image.gif)  

**Now, let's see INNER JOIN for all columns example:**  
To get all the columns from <u>foods</u> and <u>company</u> table after joining, with the following condition:

 1. **company_id** of <u>foods</u> and **company_id** of u>company</u> table must be same.

The following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    *
FROM foods JOIN company
ON
    foods.company_id =company.company_id;
```

**OUTPUT:**  
```sql
+---------+--------------+-----------+------------+------------+---------------+--------------+
| item_id | item_name    | item_unit | company_id | company_id | company_name  | company_city |
+---------+--------------+-----------+------------+------------+---------------+--------------+
|       1 | Chex Mix     | Pcs       |         16 |         16 | Akas Foods    | Delhi        |
|       2 | BN Biscuit   | Pcs       |         15 |         15 | Jack Hill Ltd | London       |
|       3 | Mighty Munch | Pcs       |         17 |         17 | Foodies       | London       |
|       4 | Pot Rice     | Pcs       |         15 |         15 | Jack Hill Ltd | London       |
|       5 | Jaffa Cakes  | Pcs       |         18 |         18 | Order All     | Boston       |
|       6 | Cheez-It     | Pcs       |         15 |         15 | Jack Hill Ltd | London       |
+---------+--------------+-----------+------------+------------+---------------+--------------+
```

---

<div id="natural-join"></div>

## NATURAL JOIN

We have already learned that an EQUI JOIN performs a JOIN against equality or matching column(s) values of the associated tables and an equal sign (=) is used as comparison operator in the where clause to refer equality.

> **NOTE:**  
> The SQL NATURAL JOIN is a type of EQUI JOIN and is structured in such a way that, columns with the same name of associated tables will appear once only.

**Pictorial presentation of the above SQL Natural Join:**  
![img](images/natural-join-example.png)  

For example, to get all the unique columns from foods and company tables, the following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    *
FROM foods NATURAL JOIN company;
```

**OUTPUT:**  
```sql
+------------+---------+--------------+-----------+---------------+--------------+
| company_id | item_id | item_name    | item_unit | company_name  | company_city |
+------------+---------+--------------+-----------+---------------+--------------+
|         16 |       1 | Chex Mix     | Pcs       | Akas Foods    | Delhi        |
|         15 |       2 | BN Biscuit   | Pcs       | Jack Hill Ltd | London       |
|         17 |       3 | Mighty Munch | Pcs       | Foodies       | London       |
|         15 |       4 | Pot Rice     | Pcs       | Jack Hill Ltd | London       |
|         18 |       5 | Jaffa Cakes  | Pcs       | Order All     | Boston       |
|         15 |       6 | Cheez-It     | Pcs       | Jack Hill Ltd | London       |
+------------+---------+--------------+-----------+---------------+--------------+
```

---

<div id="cross-join"></div>

## CROSS JOIN

The SQL **CROSS JOIN** produces a result set which is the number of rows in the first table multiplied by the number of rows in the second table <u>if no WHERE clause is used</u> along with CROSS JOIN.

> This kind of result is called as **<u>Cartesian Product</u>**.

**NOTE:**  
If **WHERE** clause is used with **CROSS JOIN**, it functions like an **INNER JOIN**.

**Pictorial Presentation of SQL Cross Join syntax:**  
![img](images/cross-join-round.png)  

To get item name and item unit columns from foods table and company name, company city columns from company table, after a CROSS JOINING with these mentioned tables, the following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    foods.item_name, foods.item_unit,
    company.company_name, company.company_city
FROM foods CROSS JOIN company;
```

or...

**INPUT:**  
```sql
SELECT
    foods.item_name, foods.item_unit,
    company.company_name, company.company_city
FROM foods, company;
```

**How cross joining happend into two tables:**  
![img](images/cross-join-example.png)  

**OUTPUT:**  
```sql
+--------------+-----------+---------------+--------------+
| item_name    | item_unit | company_name  | company_city |
+--------------+-----------+---------------+--------------+
| Chex Mix     | Pcs       | sip-n-Bite    | New York     |
| Chex Mix     | Pcs       | Order All     | Boston       |
| Chex Mix     | Pcs       | Foodies       | London       |
| Chex Mix     | Pcs       | Akas Foods    | Delhi        |
| Chex Mix     | Pcs       | Jack Hill Ltd | London       |
| BN Biscuit   | Pcs       | sip-n-Bite    | New York     |
| BN Biscuit   | Pcs       | Order All     | Boston       |
| BN Biscuit   | Pcs       | Foodies       | London       |
| BN Biscuit   | Pcs       | Akas Foods    | Delhi        |
| BN Biscuit   | Pcs       | Jack Hill Ltd | London       |
| Mighty Munch | Pcs       | sip-n-Bite    | New York     |
| Mighty Munch | Pcs       | Order All     | Boston       |
| Mighty Munch | Pcs       | Foodies       | London       |
| Mighty Munch | Pcs       | Akas Foods    | Delhi        |
| Mighty Munch | Pcs       | Jack Hill Ltd | London       |
| Pot Rice     | Pcs       | sip-n-Bite    | New York     |
| Pot Rice     | Pcs       | Order All     | Boston       |
| Pot Rice     | Pcs       | Foodies       | London       |
| Pot Rice     | Pcs       | Akas Foods    | Delhi        |
| Pot Rice     | Pcs       | Jack Hill Ltd | London       |
| Jaffa Cakes  | Pcs       | sip-n-Bite    | New York     |
| Jaffa Cakes  | Pcs       | Order All     | Boston       |
| Jaffa Cakes  | Pcs       | Foodies       | London       |
| Jaffa Cakes  | Pcs       | Akas Foods    | Delhi        |
| Jaffa Cakes  | Pcs       | Jack Hill Ltd | London       |
| Cheez-It     | Pcs       | sip-n-Bite    | New York     |
| Cheez-It     | Pcs       | Order All     | Boston       |
| Cheez-It     | Pcs       | Foodies       | London       |
| Cheez-It     | Pcs       | Akas Foods    | Delhi        |
| Cheez-It     | Pcs       | Jack Hill Ltd | London       |
| Salt n Shake | Pcs       | sip-n-Bite    | New York     |
| Salt n Shake | Pcs       | Order All     | Boston       |
| Salt n Shake | Pcs       | Foodies       | London       |
| Salt n Shake | Pcs       | Akas Foods    | Delhi        |
| Salt n Shake | Pcs       | Jack Hill Ltd | London       |
+--------------+-----------+---------------+--------------+
```

**More presentaion of the said output:**  
![img](images/cross-join-combine.png)  

---

<div id="outer-join"></div>

## OUTER JOIN

The SQL **OUTER JOIN** returns all rows from both the participating tables which satisfy the join condition along with rows which do not satisfy the join condition.

**NOTE:**  
The SQL **OUTER JOIN** operator (+) is used only on one side of the join condition only.

**Pictorial Presentation of SQL Outer Join:**  
![img](images/pictorial-representation-of-sql-outer-join.png)  

**The subtypes of SQL OUTER JOIN:**
 - LEFT OUTER JOIN or LEFT JOIN
 - RIGHT OUTER JOIN or RIGHT JOIN
 - FULL OUTER JOIN

For example, to get company name and company id columns from company table and company id, item name, item unit columns from foods table, after an OUTER JOINING with these mentioned tables, the following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    company.company_name, company.company_id,
    foods.company_id, foods.item_name, foods.item_unit
FROM company, foods
WHERE
    company.company_id = foods.company_id(+);
```

**OUTPUT:**  
```sql
COMPANY_NAME    COMPANY_ID COMPANY_ID ITEM_NAME       ITEM_UNIT
--------------- ---------- ---------- --------------- ----------
Akas Foods      16         16         Chex Mix        Pcs
Jack Hill Ltd   15         15         Cheez-It        Pcs
Jack Hill Ltd   15         15         BN Biscuit      Pcs
Foodies.        17         17         Mighty Munch    Pcs
Jack Hill Ltd   15         15         Pot Rice        Pcs
Order All       18         18         Jaffa Cakes     Pcs
sip-n-Bite.     19
```

**NOTE:**  
 - This SQL statement would return all rows from the company table and only those rows from the foods table where the joined fields are equal.
 - The (+) after the foods.company_id field indicates that, if a company_id value in the company table does not exist in the foods table, all fields in the foods table will be displayed as NULL in the result set.

---

<div id="left-join"></div>

## LEFT JOIN

The SQL **LEFT JOIN** (specified with the keywords LEFT JOIN and ON) joins two tables and fetches all matching rows of two tables for which the SQL-expression is true, plus rows from the frist table that do not match any row in the second table.

**Pictorial presentation of SQL Left Join:**  
![img](images/sql-left-jon.png)  

For example, To get **company_id** and **company_name** columns from <u>company</u> table and **company_id**, **item_name**, **item_unit** columns from <u>foods</u> table, after an OUTER JOINING with these mentioned tables, the following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    company.company_id, company.company_name, company.company_city,
    foods.company_id, foods.item_name, foods.item_unit
FROM company LEFT JOIN foods
ON
    company.company_id = foods.company_id;
```

**OUTPUT:**  
```sql
+------------+---------------+--------------+------------+--------------+-----------+
| company_id | company_name  | company_city | company_id | item_name    | item_unit |
+------------+---------------+--------------+------------+--------------+-----------+
|         15 | Jack Hill Ltd | London       |         15 | Cheez-It     | Pcs       |
|         15 | Jack Hill Ltd | London       |         15 | Pot Rice     | Pcs       |
|         15 | Jack Hill Ltd | London       |         15 | BN Biscuit   | Pcs       |
|         16 | Akas Foods    | Delhi        |         16 | Chex Mix     | Pcs       |
|         17 | Foodies       | London       |         17 | Mighty Munch | Pcs       |
|         18 | Order All     | Boston       |         18 | Jaffa Cakes  | Pcs       |
|         19 | sip-n-Bite    | New York     |       NULL | NULL         | NULL      |
+------------+---------------+--------------+------------+--------------+-----------+
```

**Explanation:**  
This SQL statement would return all rows from the company table and only those rows from the foods table where the joined fields are equal and if the ON clause matches no records in the 'foods' table, the join will still return rows, but the NULL in each column of the right table.

**Pictorial Presentation of the above example SQL Left Join:**  
![img](images/sql-left-join-set-image.png)  

---

<div id="right-join"></div>

## RIGHT JOIN

The SQL RIGHT JOIN, joins two tables and fetches rows based on a condition, which is matching in both the tables ( before and after the JOIN clause mentioned in the syntax below) , and the unmatched rows will also be available from the table written after the JOIN clause.

**Pictorial presentation of SQL Right Join:**  
![img](images/sql-right-jon.gif)  

For example, to get **company_id**, **company_name** and **company_city** columns from <u>company</u> table and **company_id**, **item_name** columns from <u>foods</u> table, after an OUTER JOINING with these mentioned tables, the following SQL statement can be used:

**INPUT:**  
```sql
SELECT
    company.company_id, company.company_name, company.company_city,
    foods.company_id, foods.item_name
FROM company RIGHT JOIN foods
ON
    company.company_id = foods.company_id;
```

**OUTPUT:**  
```sql
+------------+---------------+--------------+------------+--------------+
| company_id | company_name  | company_city | company_id | item_name    |
+------------+---------------+--------------+------------+--------------+
|         16 | Akas Foods    | Delhi        |         16 | Chex Mix     |
|         15 | Jack Hill Ltd | London       |         15 | BN Biscuit   |
|         17 | Foodies       | London       |         17 | Mighty Munch |
|         15 | Jack Hill Ltd | London       |         15 | Pot Rice     |
|         18 | Order All     | Boston       |         18 | Jaffa Cakes  |
|         15 | Jack Hill Ltd | London       |         15 | Cheez-It     |
|       NULL | NULL          | NULL         |       NULL | Salt n Shake |
+------------+---------------+--------------+------------+--------------+
```

**Pictorial Presentation of the above example:**  
![img](images/sql-right-join-set-image.gif)  

---

<div id="full-outer-join"></div>

## FULL OUTER JOIN

In SQL the **FULL OUTER JOIN** combines the results of both **left** and **right outer joins** and returns all (matched or unmatched) rows from the tables on both sides of the join clause.

**Pictorial Presentation: SQL Full Outer Join**  
![img](images/sql-full-outer-join.gif)  
![img](images/sql-full-outer-join-slide-1.png)  
![img](images/sql-full-outer-join-slide-2.png)  

**Example: SQL Full Outer Join**  
Let’s combine the same two tables using a full join.

![img](images/sql-full-outer-join-sample-table.png)  

**INPUT:**  
```sql
SELECT
    *
FROM table_A FULL OUTER JOIN table_B 
ON
    table_A.A = table_B.A;
```

**OUTPUT:**  
![img](images/sql-full-outer-join-output-image1.png)  

Because this is a full join, all rows (both matching and nonmatching) from both tables are included in the output. There is only one match between table table_A and table table_B, so **only one row of output displays values in all columns**. All remaining rows of output contain only values from table table_A or table table_B, with the remaining columns set to missing values

**Only one row of output displays values in all columns explain below:**
![img](images/sql-full-outer-join-output-image2.png)  

**NOTE:**  
As we know the **FULL OUTER JOIN** is the combination of the results of both **LEFT OUTER JOIN** and **RIGHT OUTER JOIN**, so, here we are going to describe how **FULL OUTER JOIN** perform internally.

**Pictorial Presentation SQL Full Outer Join:**  
![img](images/left-right-full-outer-join.png)  

---

<div id="join-vs-inner-join"></div>

## Difference between "JOIN" and "INNER JOIN"

 - **JOIN:**
   - JOIN returns all rows from tables where the key record of one table is equal to the key records of another table.
 - **INNER JOIN:**
   - O INNER JOIN seleciona todas as linhas de ambas as tabelas participantes, desde que haja correspondência entre as colunas. Um SQL INNER JOIN é o mesmo que uma cláusula JOIN, combinando linhas de duas ou mais tabelas.

---

<div id="nj-ij"></div>

## Difference between "NATURAL JOIN" and "INNER JOIN"

There is one significant difference between **INNER JOIN** and **NATURAL JOIN** is the number of columns returned.

See the following example on company table and foods table:

**INPUT:**  
```sql
SELECT
    *
FROM company INNER JOIN foods
ON
    company.company_id = foods.company_id;
```

**OUTPUT:**  
```sql
+------------+---------------+--------------+---------+--------------+-----------+------------+
| company_id | company_name  | company_city | item_id | item_name    | item_unit | company_id |
+------------+---------------+--------------+---------+--------------+-----------+------------+
|         16 | Akas Foods    | Delhi        |       1 | Chex Mix     | Pcs       |         16 |
|         15 | Jack Hill Ltd | London       |       2 | BN Biscuit   | Pcs       |         15 |
|         17 | Foodies       | London       |       3 | Mighty Munch | Pcs       |         17 |
|         15 | Jack Hill Ltd | London       |       4 | Pot Rice     | Pcs       |         15 |
|         18 | Order All     | Boston       |       5 | Jaffa Cakes  | Pcs       |         18 |
|         15 | Jack Hill Ltd | London       |       6 | Cheez-It     | Pcs       |         15 |
+------------+---------------+--------------+---------+--------------+-----------+------------+
```

**NOTE:**  
See that INNER JOIN return all columns from company and foods tables *(Including duplicate "company_id" columns)*.

**INPUT:**  
```sql
SELECT
    *
FROM company NATURAL JOIN foods;
```

**OUTPUT:**  
```sql
+------------+---------------+--------------+---------+--------------+-----------+
| company_id | company_name  | company_city | item_id | item_name    | item_unit |
+------------+---------------+--------------+---------+--------------+-----------+
|         16 | Akas Foods    | Delhi        |       1 | Chex Mix     | Pcs       |
|         15 | Jack Hill Ltd | London       |       2 | BN Biscuit   | Pcs       |
|         17 | Foodies       | London       |       3 | Mighty Munch | Pcs       |
|         15 | Jack Hill Ltd | London       |       4 | Pot Rice     | Pcs       |
|         18 | Order All     | Boston       |       5 | Jaffa Cakes  | Pcs       |
|         15 | Jack Hill Ltd | London       |       6 | Cheez-It     | Pcs       |
+------------+---------------+--------------+---------+--------------+-----------+
```

**NOTE:**  
See that now we don't have duplicate columns (like "company_id").

---

<div id="on-where"></div>

## Difference between WHERE and ON in SQL

 - **ON:**
   - ON should be used to define the join condition.
 - **WHERE:**
   - WHERE should be used to filter the data.

---

<div id="diagrams"></div>

## JOIN and Veen Diagrams

Now, let's see some **JOIN** and **Veen Diagrams**:

![img](images/join-diagrams-01.jpg_large)  

---

**REFERENCES:**  
[Difference between WHERE and ON in SQL](https://dataschool.com/how-to-teach-people-sql/difference-between-where-and-on-in-sql/)
[SQL Inner Join](https://www.w3resource.com/sql/joins/perform-an-inner-join.php)  
[SQL Natural Join](https://www.w3resource.com/sql/joins/natural-join.php)
[SQL Cross Join](https://www.w3resource.com/sql/joins/cross-join.php)
[SQL Outer Join](https://www.w3resource.com/sql/joins/perform-an-outer-join.php)
[SQL Left Join](https://www.w3resource.com/sql/joins/perform-a-left-join.php)
[SQL Right Join](https://www.w3resource.com/sql/joins/perform-a-right-join.php)
[SQL Full Outer Join](https://www.w3resource.com/sql/joins/perform-a-full-outer-join.php)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
