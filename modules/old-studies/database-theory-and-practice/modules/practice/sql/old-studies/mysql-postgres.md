# Contents

 - **CRUD (Create, Read, Update, Delete):**
   - **Create:**
     - [CREATE DATABASE](#create-database)
     - [CREATE TABLE table_name](#create-table)
   - **Read:**
     - [SHOW TABLES or \dt](#show-tables)
   - **Update:**
   - **Delete:**
     - [DROP DATABASE db_name](#drop-database)
 - **Useful commands:**
   - [SHOW DATABASES or \l](#show-databases)
   - [USE db_name or \c db_name](#use-db_name)
   - [What database we are using? ( SELECT database() or SELECT current_database() )](#qdqau)
 - **Settings:**
   - [Docker composes (MySQL, PostgreSQL)](#settings-docker-composes)

<!--- ( CRUD/Create ) --->

---

<div id="create-database"></div>

## CREATE DATABASE

To create a database on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
CREATE DATABASE db_name;
```

**PostgreSQL:**
```sql
CREATE DATABASE dbname;
```

> **NOTE:**  
> The PostgreSQL database doesn't support composed name using "-".
> ERROR: db-name
> OK: db_name

---

<div id="create-table"></div>

## CREATE TABLE table_name

To *create tables* on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
CREATE TABLE tbl_book (
  ID_Book SMALLINT AUTO_INCREMENT PRIMARY KEY,
  Book_name VARCHAR(50) NOT NULL,
  ISBN VARCHAR(30) NOT NULL,
  ID_AUTHOR SMALLINT NOT NULL,
  DATA_PUB DATE NOT NULL,
  BOOK_PRICE DECIMAL NOT NULL
);

CREATE TABLE tbl_authors (
  ID_AUTHOR SMALLINT PRIMARY KEY,
  AUTHOR_NAME VARCHAR(50),
  AUTHOR_SURNAME VARCHAR(50)
);

CREATE TABLE tbl_publishers (
  PUBLISHER_ID SMALLINT PRIMARY KEY AUTO_INCREMENT,
  PUBLISHER_NAME VARCHAR(50) NOT NULL
);
```

> **NOTE:**  
> - To implement **"AUTO_INCREMENT"** in PostgreSQL uses **"SERIAL"**.

**PostgreSQL:**
```sql
CREATE TABLE tbl_book (
  ID_Book SERIAL PRIMARY KEY,
  Book_name VARCHAR(50) NOT NULL,
  ISBN VARCHAR(30) NOT NULL,
  ID_AUTHOR SMALLINT NOT NULL,
  DATA_PUB DATE NOT NULL,
  BOOK_PRICE DECIMAL NOT NULL
);

CREATE TABLE tbl_authors (
  ID_AUTHOR SMALLINT PRIMARY KEY,
  AUTHOR_NAME VARCHAR(50),
  AUTHOR_SURNAME VARCHAR(50)
);

CREATE TABLE tbl_publishers (
  PUBLISHER_ID SERIAL PRIMARY KEY,
  PUBLISHER_NAME VARCHAR(50) NOT NULL
);
```








































<!--- ( CRUD/Read ) --->

---

<div id="show-tables"></div>

## SHOW TABLES or \dt

To see the tables of the current database we are using on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
SHOW TABLES;
```

**PostgreSQL:**
```sql
\dt
```








































<!--- ( CRUD/Update ) --->








































<!--- ( CRUD/Delete ) --->

---

<div id="drop-database"></div>

## DROP DATABASE db_name

To delete a Database on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
DROP DATABASE db_name;
```

**PostgreSQL:**
```sql
DROP DATABASE db_name;
```

> **NOTE:**  
> In the case of the **"DROP DATABASE"** statement, it is used to completely delete an entire database, including all tables, records, and other objects related to it.








































<!--- ( Useful commands ) --->

---

<div id="show-databases"></div>

## SHOW DATABASES or \l

To show the databases on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
SHOW DATABASES;
```

**PostgreSQL:**
```sql
\l
```

---

<div id="use-db_name"></div>

## USE db_name or \c db_name

To use a exists database on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
USE db_name;
```

**PostgreSQL:**
```sql
\c db_name
```

---

<div id="qdqau"></div>

## What database we are using? ( SELECT database() or SELECT current_database() )

To show (know) what database you are using on **MySQL** or **PostgreSQL** you can use the following commands:

**MySQL:**
```sql
SELECT database();
```

**OUTPUT:**
```sql
+------------+
| database() |
+------------+
| NULL       |
+------------+
1 row in set (0.00 sec)
```

> **NOTE:**  
> In MySQL if you are not using any the return is NULL.


**PostgreSQL:**
```sql
SELECT current_database();
```








































<!--- ( Settings/Docker composes ) --->

---

<div id="settings-docker-composes"></div>

## Docker composes (MySQL, PostgreSQL)

The first thing you need is to install the containers:

```bash
sudo docker compose up -d
```

### MySQL Docker Compose

```bash
sudo docker exec -it mysql-container bash
```

```bash
mysql --user=root --password=toor
```

### PostgreSQL Docker Compose

```bash
sudo docker exec -it postgres-container bash
```

```bash
psql -U postgres
```
