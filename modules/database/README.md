# Database (Theory and Practice)

## Contents

 - **PostgreSQL:**
   - [**PostgreSQL Settings**](#postgresql-settings)
   - **Useful Commands:**
     - [`List databases (\l or \list)`](#list-databases)
     - [`Connect to a database (\c or \connect)`](#connect-database)
     - [`Display Tables (\dt or \dt+)`](#display-tables)
   - **CRUD (Create, Read, Update, Delete):**
     - **CREATE:**
       - [`CREATE DATABASE`](#create-database)
       - [`CREATE TABLE`](#create-table)
     - **READ:**
     - **UPDATE:**
     - **DELETE:**
       - [`DROP DATABASE`](#drop-database)
       - [`DROP TABLE`](#drop-table)
 - [**Database (Old Studies)**](https://github.com/rodrigols89/studies/tree/old-studies/modules/old-studies/database-theory-and-practice)
 - [**REFERENCES**](#ref)
<!--- 
[WHITESPACE RULES]
- Same topic = "20" Whitespace character.
- Different topic = "50" Whitespace character.
--->













































































<!--- ( PostgreSQL/Settings ) --->

---

## <div id="postgresql-settings"></div>

## PostgreSQL Settings

**Run docker compose:**
```bash
sudo docker compose up -d
```

**Enter the container:**
```bash
sudo docker exec -it postgres-container bash
```

**Enter the psql:**
```bash
psql -h localhost -U postgres
```

**Exit from the psql:**
```bash
exit
```




















<!--- ( PostgreSQL/Useful Commands ) --->

---

<div id="list-databases"></div>

## `List databases (\l or \list)`

To list all databases in Postgres using **psql**, you can use the **"\l"** or **"\list"** command.

 - The database name.
 - The owner of the database.
 - The encoding for the database.
 - The collation for the database.

For example:

**INTPUT:**  
```bash
\l
```

**OUTPUT:**  
```bash
   Name    | Owner | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider | Access privileges 
-----------+-------+----------+------------+------------+------------+-----------------+-------------------
 postgres  | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 root      | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/root          +
           |       |          |            |            |            |                 | root=CTc/root
 template1 | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/root          +
           |       |          |            |            |            |                 | root=CTc/root
(4 rows)
```

---

<div id="connect-database"></div>

## `Connect to a database (\c or \connect)`

To connect to a existing database, you can use the `\c` or `\connect` command:

**INTPUT:**  
```bash
\c mydb
```

**OUTPUT:**  
```bash
You are now connected to database "mydb" as user "root".
```

---

<div id="display-tables"></div>

## `Display Tables (\dt or \dt+)`

To list all tables in a database, we can use the `\dt (display tables)` or `\dt+` command:

**INTPUT:**
```bash
\dt+
```

**OUTPUT:**
```bash
                                      List of relations
 Schema |  Name   | Type  |  Owner   | Persistence | Access method |    Size    | Description 
--------+---------+-------+----------+-------------+---------------+------------+-------------
 public | student | table | postgres | permanent   | heap          | 8192 bytes | 
(1 row)
```

> **NOTE:**
> The command `\dt+` will also display the size of each table.




















<!--- ( PostgreSQL/CRUD/CREATE ) --->

---

<div id="create-database"></div>

## `CREATE DATABASE`

To create a database, we can use the `CREATE DATABASE dbname;` statement:

**INTPUT:**  
```bash
CREATE DATABASE dbname;
```

**OUTPUT:**  
```bash
CREATE DATABASE
```

---

<div id="create-table"></div>

## `CREATE TABLE`

To create a table, we can use the `CREATE TABLE table_name (column1 datatype, column2 datatype, ...);` statement:

**EXAMPLE:**  
```
CREATE TABLE Student(
    id int,
    name text,
    age int,
    address char(30)
);
```

**OUTPUT:**  
```
CREATE TABLE
```




















<!--- ( PostgreSQL/CRUD/READ ) --->
<!--- ( PostgreSQL/CRUD/UPDATE ) --->




















<!--- ( PostgreSQL/CRUD/DELETE ) --->

---

<div id="drop-database"></div>

## `DROP Database`

To delete a database, we can use the **DROP DATABASE** command:

**INTPUT:**
```bash
DROP DATABASE IF EXISTS dbname;
```

**OUTPUT:**
```bash
DROP DATABASE
```

**WITH (FORCE):**  
The **WITH (FORCE)** option is available in PostgreSQL version 13 and higher. The **DROP DATABASE** method won't remove the database if it's in use. If the database is in use, the terminal prints an error that a database session is open.

Add the **WITH (FORCE)** option to forcefully close the session and delete the database:

**INTPUT:**
```bash
DROP DATABASE IF EXISTS dbname WITH (FORCE);
```

**OUTPUT:**  
```bash
DROP DATABASE
```

---

<div id="drop-table"></div>

## `DROP TABLE`

To understand how to delete a table, let's imagine we have the following table:

```bash
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | student | table | postgres
```

Now, to delete the table, we can use the **DROP TABLE** command following the syntax:

**INTPUT:**
```bash
DROP TABLE IF EXISTS schema_name."table_name";
```

For example, for our `student` table, we can use the following command:

**INTPUT:**
```bash
DROP TABLE IF EXISTS public."student";
```

**OUTPUT:**
```bash
DROP TABLE
```










































































































<!--- ( REFERENCES ) --->

---

<div id="ref"></div>

## REFERENCES

 - **General:**
   - [Google Gemini](https://gemini.google.com/app)
   - [ChatGPT](https://chatgpt.com/)
 - **PostgreSQL:**
   - **FUNDAMENTALS:**
     - [PostgreSQL Data Types](https://www.w3resource.com/PostgreSQL/data-types.php)
     - [PostgreSQL CONSTRAINTS](https://www.w3resource.com/PostgreSQL/constraint.php)
   - **CREATE:**
     - [PostgreSQL Create Database](https://www.javatpoint.com/postgresql-create-database)
     - [PostgreSQL Create Table](https://www.javatpoint.com/postgresql-create-table)
   - **READ:**
     - [How to List Databases Using the psql command line tool](https://www.beekeeperstudio.io/blog/how-to-list-databases-in-postgres#:~:text=To%20list%20all%20databases%20in,each%20database%20on%20the%20server.)
     - [PostgreSQL WHERE](https://www.w3resource.com/PostgreSQL/where.php)
     - [PostgreSQL GROUP BY](https://www.w3resource.com/PostgreSQL/postgresql-group-by.php)
     - [PostgreSQL HAVING](https://www.w3resource.com/PostgreSQL/postgresql-having.php)
     - [PostgreSQL JOIN](https://www.w3resource.com/PostgreSQL/postgresql-join.php)
     - [PostgreSQL CROSS JOIN](https://www.w3resource.com/PostgreSQL/postgresql-cross-join.php)
     - [PostgreSQL INNER JOIN](https://www.w3resource.com/PostgreSQL/postgresql-inner-join.php)
     - [PostgreSQL LEFT JOIN or LEFT OUTER JOIN](https://www.w3resource.com/PostgreSQL/postgresql-left-join.php)
     - [PostgreSQL RIGHT JOIN or RIGHT OUTER JOIN](https://www.w3resource.com/PostgreSQL/postgresql-right-join.php)
     - [PostgreSQL FULL OUTER JOIN](https://www.w3resource.com/PostgreSQL/postgresql-full-outer-join.php)
   - **UPDATE:**
   - **DELETE:**
     - [PostgreSQL Delete/Drop Database](https://www.javatpoint.com/postgresql-drop-database)
     - [PostgreSQL Drop/Delete Table](https://www.javatpoint.com/postgresql-drop-table)
   - **Settings:**
     - [Setting up PgAdmin Docker Connection: 3 Critical Steps](https://hevodata.com/learn/pgadmin-docker/)
     - [Connect to PostgreSQL Database on Linux, Windows](https://www.w3resource.com/PostgreSQL/connect-to-postgresql-database.php)
     - [Install PostgreSQL on Linux and Windows](https://www.w3resource.com/PostgreSQL/install-postgresql-on-linux-and-windows.php)

---

**Rodrigo** **L**eite da **S**ilva
