# Structured Query Language (SQL)

## Contents

 - **SELECT:**
   - [1757. Recyclable and Low Fat Products](#1757-ralfp)
 - **JOIN:**
   - [1378. Replace Employee ID With The Unique Identifier](#1378-reiwtui)
 - **Tips and Tricks:**
<!---
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "200" Whitespace character.
--->









































































































<!--- ( SELECT ) --->

---

<div id="1757-ralfp"></div>

## 1757. Recyclable and Low Fat Products

**Table: Products**
```bash
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
```

 - `product_id` is the primary key (column with unique values) for this table.
 - `low_fats` is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
 - `recyclable` is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

> Write a solution to find the ids of products that are both low fat and recyclable.  
> Return the result table in any order.

The result format is in the following example.

**INPUT:**
```bash
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
```

**OUTPUT:**
```bash
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
```

**Explanation:**  
Only products 1 and 3 are both low fat and recyclable.

<details>

<summary>RESPOSTA (PostgreSQL)</summary>

<br/>

Para começar a resolver essa questão vamos identificar quais variáveis (ou colunas do banco de dados) nós temos para trabalhar:

 - `product_id`
   - Que representa o ID do produto e também é a chave primária.
 - `low_fats`
   - Que é um ENUM (categoria) de tipos ('Y', 'N') onde:
     - 'Y' significa que esse produto é low fat;
     - 'N' significa que ele não é low fat.
 - `recyclable`
   - Que é um ENUM (categoria) de tipos ('Y', 'N') onde:
     - 'Y' significa que esse produto é reciclável;
     - 'N' significa que ele não é reciclável.

Agora que nós já sabemos quais variáveis temos, vamos para a questão (pergunta):

> Write a solution to find the ids of products that are both low fat and recyclable.  
> Return the result table in any order.

 - Ou seja, queremos encontrar os IDs dos produtos que sejam **low fat** e **recicláveis** (ao mesmo tempo `and`).

```sql
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

</details>

**REFERENCE:**  
[1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description/)









































































































<!--- ( JOIN ) --->

---

<div id="1378-reiwtui"></div>

## 1378. Replace Employee ID With The Unique Identifier

**Table: Employees**
```bash
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
```

 - `id` is the primary key (column with unique values) for this table.
 - Each row of this table contains the `id` and the `name` of an employee in a company.

**Table: EmployeeUNI**
```bash
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
```

 - `(id, unique_id)` is the primary key (combination of columns with unique values) for this table.
 - Each row of this table contains the `id` and the corresponding `unique id` of an employee in the company.

> Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.  
> Return the result table in any order.

The result format is in the following example.

**INPUT:**
```bash 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+

EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
```

**OUTPUT:**
```bash
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
```

**Explanation:**

 - Alice and Bob do not have a unique ID, We will show null instead.
 - The unique ID of Meir is 2.
 - The unique ID of Winston is 3.
 - The unique ID of Jonathan is 1.

<details>

<summary>RESPOSTA (PostgreSQL)</summary>

<br/>

Para começar a resolver essa questão vamos identificar quais variáveis (ou colunas do banco de dados) nós temos para trabalhar:

 - `Tabela Employees`
   - `id`
     - Que representa o ID do funcionário e também é a chave primária.
   - `name`
     - Que representa o nome do funcionário.
 - `Tabela EmployeeUNI`
   - `id`
     - Que representa o ID do funcionário e também é a chave primária.
   - `unique_id`
     - Que representa o ID exclusivo do funcionário.

Agora que nós já sabemos quais variáveis temos, vamos para a questão (pergunta):

> Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.  
> Return the result table in any order.

 - Ou seja, queremos encontrar os IDs exclusivos dos funcionários.

De início vamos selecionar quais variáveis (colunas) nós queremos exibir:

```sql
SELECT unique_id, name
```

Continuando, agora vamos selecionar apenas os dados que aparecem na tabela esquerda (LEFT JOIN), ou seja, os dados da tabela `Employees`.

```sql
SELECT unique_id, name
FROM Employees LEFT JOIN EmployeeUNI
```

Por fim, vamos adicionar uma condição (ON) de busca:

```sql
SELECT unique_id, name
FROM Employees LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;
```

</details>

**REFERENCE:**  
[1378. Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/)










































































































---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**

<details>

<summary></summary>

<br/>

RESPOSTA

```bash

```

![img](images/)  

</details>
