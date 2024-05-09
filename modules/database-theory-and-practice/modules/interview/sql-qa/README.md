# SQL (Q&A)

## Contents

 - **Select:**
   - [Recyclable and Low Fat Products](#select-1757)
 - **Joins:**
 - **Aggregate Functions:**
 - **Sorting and Grouping:**
 - **Subqueries:**
 - **String Functions / Regex / Clause:**




































































































<!--- ( Select ) --->

---

<div id="select-1757"></div>

## Recyclable and Low Fat Products

Imagine we have the following table:

```sql
Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
```

Where:

 - **"product_id"** is the primary key (column with unique values) for this table.
 - **"low_fats"** is an ENUM (category) of type ('Y', 'N') where:
   - 'Y' means this product is low fat.
   - 'N' means it is not.
 - **"recyclable"** is an ENUM (category) of types ('Y', 'N') where:
   - 'Y' means this product is recyclable.
   - 'N' means it is not.

Now...

> **Write a solution to find the ids of products that are both "low fat" and "recyclable".**  
> **NOTE:** Return the result table in any order.

**SOLUTION:**  
```sql
select product_id from products where low_fats ='Y' and recyclable = 'Y'
```

**OUTPUT:**  
```sql
Input
Products =
| product_id | low_fats | recyclable |
| ---------- | -------- | ---------- |
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |
| 4          | N        | N          |

Output
| product_id |
| ---------- |
| 1          |
| 3          |

Expected
| product_id |
| ---------- |
| 1          |
| 3          |
```

**REFERENCE:**  
[1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/)



































































































---

**Rodrigo** **L**eite da **S**ilva
