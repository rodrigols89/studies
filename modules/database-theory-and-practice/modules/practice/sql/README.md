# SQL

## Contents

 - **Useful commands:**
   - [SHOW DATABASES or \l](#show-databases)
   - [USE db_name or \c db_name](#use-db_name)
   - [What database we are using? ( SELECT database() or SELECT current_database() )](#qdqau)
 - **CRUD (Create, Read, Update, Delete):**
   - **Create:**
     - [CREATE DATABASE](#create-database)
   - **Read:**
   - **Update:**
   - **Delete:**
 - **Settings:**
   - [Docker composes (MySQL, PostgreSQL)](#settings-docker-composes)
 - [**References**](#References)

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








































<!--- ( CRUD/Read ) --->

---

<div id=""></div>

## x

x








































<!--- ( CRUD/Update ) --->

---

<div id=""></div>

## x

x








































<!--- ( CRUD/Delete ) --->

---

<div id=""></div>

## x

x














































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









































<!--- ( References ) --->

---

<div id="ref"></div>

## References

 - []()

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
