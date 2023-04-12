# PostgreSQL

## Contents

 - [List databases (\l)](#list-databases)
 - **Settings:**
   - [Docker Compose Settings](#docker-compose-settings)
 - [References](#references)

---

<div id="list-databases"></div>

## List databases (\l)

To list all databases in Postgres using **psql**, you can use the **"\l"** command. This command will display a table with information about each database, including:

 - The database name.
 - The owner of the database.
 - The encoding for the database.
 - The collation for the database.

For example:

**INTPUT:**  
```
\l
```

**OUTPUT:**  
```
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

<div id="docker-compose-settings"></div>

## Docker Compose Settings

I strongly recommender install Docker container that contains **PostgreSQL** installed:

```
sudo docker compose up -d
```

Now, only enter into **PostgreSQL** into the container:

```
sudo docker exec -it postgres-container bash
```

Finally, to run the **PostgreSQL** inside the container run:

```
psql
```

To quit run:

```
exit
```

**NOTE:**  
You can also open the **"pgAdmin 4"** on the browser to test your database queries:

 - **URLs:**
   - [http://localhost:8080](http://localhost:8080) or [http://127.0.0.1:8080](http://127.0.0.1:8080)
 - **Email/User:**
   - `admin@admin.com`
 - **Password:**
   - secret

---

<div id="references"></div>

## References

 - [PostgreSQL Data Types](https://www.w3resource.com/PostgreSQL/data-types.php)
 - [PostgreSQL CONSTRAINTS](https://www.w3resource.com/PostgreSQL/constraint.php)
 - **Settings:**
   - [Setting up PgAdmin Docker Connection: 3 Critical Steps](https://hevodata.com/learn/pgadmin-docker/)
   - [Connect to PostgreSQL Database on Linux, Windows](https://www.w3resource.com/PostgreSQL/connect-to-postgresql-database.php)
   - [Install PostgreSQL on Linux and Windows](https://www.w3resource.com/PostgreSQL/install-postgresql-on-linux-and-windows.php)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

**INTPUT:**  
```

```

**OUTPUT:**  
```

```
