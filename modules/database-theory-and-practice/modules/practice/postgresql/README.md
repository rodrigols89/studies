# PostgreSQL

## Contents

 - [](#)
 - [References](#references)
 - **Settings:**
   - [Docker Compose Settings](#docker-compose-settings)

---

<div id="references"></div>

## References

 - **Settings:**
   - [Setting up PgAdmin Docker Connection: 3 Critical Steps](https://hevodata.com/learn/pgadmin-docker/)
   - [Connect to PostgreSQL Database on Linux, Windows](https://www.w3resource.com/PostgreSQL/connect-to-postgresql-database.php)
   - [Install PostgreSQL on Linux and Windows](https://www.w3resource.com/PostgreSQL/install-postgresql-on-linux-and-windows.php)

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
psql -U root
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

Ro**drigo** **L**eite da **S**ilva - **drigols**
