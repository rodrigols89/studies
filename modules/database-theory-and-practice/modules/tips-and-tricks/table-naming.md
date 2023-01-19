# Table naming (Singular vs. Plural)

## Contents

 - [Narayana “Vyas” Kondreddi approach (plural)](#narayana-approach)
 - [My personal analysis](#rdg-approach)

---

<div id="narayana-approach"></div>

## Narayana “Vyas” Kondreddi approach (plural)

Narayana “Vyas” Kondreddi (long-time DBA and SQL Engineer) wrote back in 2001:

**Tables represent the instances of an entity:**  
 - For example, you store all your **customer** information in a table:
   - Here, **‘customer’** is an entity;
   - And all the **rows in the customers** table **represent the instances** of the entity **‘customer’**.

**Answer:**  
 - So, why not name your table using the entity it represents, ‘Customer’. Since the table is storing `‘multiple instances’` of customers, make your table name a plural word.
 - It feels logical, and somewhat *“natural”*. You store several customers inside a table (those `“multiple instances”`), so the table should naturally be names ***customers***.

It also makes sense when writing an SQL statement. When you want to go through all your customers, you:

```sql
SELECT * FROM customers
```

**NOTE:**  
When using plural name, one can consider a table like a crate (caixa) containing several items. A crate (caixa) of apples should be labelled Apples, whether it contains one or a hundred apples.

---

<div id="rdg-approach"></div>

## My personal analysis

My personal analysis is the following. Imagine you have the entity **Users**:

> **NOTE:**  
> **Users table** can have on or many registers.

If I use the following select query:

```sql
SELECT id, name
FROM users;
```

**NOTE:**  
Even though the "Users" table has a single record. This entity (Users) represents a set of users that can have multiple rows.

---

**REFERENCES:**  
[The table naming dilemma: singular vs. plural](https://medium.com/@fbnlsr/the-table-naming-dilemma-singular-vs-plural-dc260d90aaff)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
