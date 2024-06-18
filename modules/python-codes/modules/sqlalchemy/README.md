# SQLAlchemy

## Contents

 - **Concepts:**
   - [create_engine() object](#create-engine)
   - [Session](#session)
 - **CRUD (CREATE, READ, UPDATE, DELETE):**
   - **CREATE:**
     - [Creating tables](#create-all)
     - [Inserting data into a table](#session-add)
     - [Inserting many registers](#session-add-all)
   - **READ:**
     - [SELECT using session.query(object)](#session-query)
   - **UPDATE:**
   - **DELETE:**
 - **Settings:**
   - [Docker composes](#settings-docker-composes)
   - [Python settings](#python-settings)
 - [**References**](#references)
<!--- 
[WHITESPACE RULES]
- Same topic = "10" Whitespace character.
- Different topic = "50" Whitespace character.
--->




















































<!--- ( Concepts ) --->

---

<div id="create-engine"></div>

## create_engine() function

> The **create_engine()** function produces an Engine object based on a URL - *That URL follows the RFC-1738*.

**URL Sintax:**  
```python
dialect+driver://username:password@host:port/database
```

For example, let's see how to create an Engine object based on a URL:

[Engine.py](src/Engine.py)
```python
from sqlalchemy import create_engine, exc


def get_engine(dialect, username, password, port, database, host="localhost"):
    try:
        engine = create_engine(
            f"{dialect}://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
    except exc.SQLAlchemyError as e:
        print("An error occurred while the Engine was initializing:", str(e))
    else:
        return engine
```

> **NOTE:**  
> The **"echo" flag** is a shortcut to set up SQLAlchemy logging, which is accomplished via Python’s standard logging module. To hide the verbose output, set echo attribute to **False/None**.

Now, let's create setting dictionaries for the **"MySQL"** and **"PostgreSQL"** databases:

[Settings.py](src/Settings.py)
```python
mysql_settings = {
    "dialect": "mysql+pymysql",
    "username": "root",
    "password": "toor",
    "port": "3310",
    "database": "mysqldb",
}

postgresql_settings = {
    "dialect": "postgresql",
    "username": "postgres",
    "password": "toor",
    "port": "5432",
    "database": "postgresdb",
}
```

Finally, let's test the **get_engine()** function:

```python
from Settings import mysql_settings, postgresql_settings
from Engine import get_engine


print("================= ( MySQL Engine ) ==================")
engine = get_engine(**mysql_settings)
print(engine)
print("type = ", type(engine))
print("bool = ", bool(engine))

print("\n============== ( PostgreSQL Engine ) ================")
engine = get_engine(**postgresql_settings)
print(engine)
print("type = ", type(engine))
print("bool = ", bool(engine))
```

**OUTPUT:**  
```python
================= ( MySQL Engine ) ==================
Engine(mysql+pymysql://root:***@localhost:3310/mysqldb)
type =  <class 'sqlalchemy.engine.base.Engine'>
bool =  True

============== ( PostgreSQL Engine ) ================
Engine(postgresql://postgres:***@localhost:5432/postgresdb)
type =  <class 'sqlalchemy.engine.base.Engine'>
bool =  True
```










<!--- ( Session ) --->

---

<div id="session"></div>

## Session

 - A **Session** object is a handle (identificador) to the database.
 - **NOTE:**  To create a Session we need to instance a **sessionmaker()** class.

For example:

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)

session = Session()
```

**NOTE:**
A good practice is to use the keyword **"with"** to create a *Session*. Thus, at the end of the **"with"** block, the *Session* is automatically terminated.

For example:

```python
with Session() as session:
    # Statements...
```

Or you can make a **"bind"** directly on the Session. For it we need to import the Session object diretly:

```python
from sqlalchemy.orm import Session
```

Now, you only need to pass a engine directly to the Session object, that's, make a **"bind=engine"**:

```python
                |
                |
               \ /
with Session(engine) as session:
    # Statements...
```





















































<!--- ( CRUD = CREATE ) --->

---

<div id="create-all"></div>

## Creating tables

> The **create_all()** method is used to create all tables stored in **MetaData (or declarative_base)**.

For example, imagine we have the classes **HeroModel** and **StudentModel** to represent tables on our database:

[SQLAlchemy_Models.py](src/SQLAlchemy_Models.py)
```python
from sqlalchemy import Column, Float, Integer, VARCHAR
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class HeroModel(Base):
    __tablename__ = "hero"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    npc_name = Column(VARCHAR(50), nullable=False)
    primary_attr = Column(VARCHAR(50), nullable=False)
    attack_type = Column(VARCHAR(50), nullable=False)
    img = Column(VARCHAR(100), nullable=False)
    icon = Column(VARCHAR(100), nullable=False)
    base_health = Column(Float, nullable=False)
    base_health_regen = Column(Float, nullable=False)
    base_mana = Column(Float, nullable=False)
    base_mana_regen = Column(Float, nullable=False)
    base_armor = Column(Float, nullable=False)
    base_attack_min = Column(Float, nullable=False)
    base_attack_max = Column(Float, nullable=False)
    base_str = Column(Float, nullable=False)
    base_agi = Column(Float, nullable=False)
    base_int = Column(Float, nullable=False)
    str_gain = Column(Float, nullable=False)
    agi_gain = Column(Float, nullable=False)
    int_gain = Column(Float, nullable=False)
    attack_range = Column(Float, nullable=False)
    projectile_speed = Column(Float, nullable=False)
    move_speed = Column(Float, nullable=False)
    legs = Column(Integer, nullable=False)


class StudentModel(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)
    lastname = Column(VARCHAR(50), nullable=False)
```

Now, we need to use the **create_all method** in **MetaData (or declarative_base for our case)** to create stored tables. For example, our "Base" object has two tables (models) stored:

 - **"hero"**;
 - and **"student"**.

Now, we only need call the **create_all method** and pass the *Engine (to access the database)* to create all tables stored in **MetaData (or declarative_base for our case)**:

[test_create_table.py](src/test_create_table.py)
```python

```

**INPUT:**  
```bash
python driver_models.py
```

**OUTPUT:**  
```bash

```










































































































<!--- ( Settings ) --->

---

<div id="settings-docker-composes"></div>

## Docker composes (MySQL, PostgreSQL)

```bash
sudo docker compose up -d
```

### MySQL Docker Compose

```bash
sudo docker exec -it mysql-container bash
```

```bash
mysql --user=root --password=toor mysql-db
```

### PostgreSQL Docker Compose

```bash
sudo docker exec -it postgres-container bash
```

```bash
psql -U postgres
```

**INPUT:**
```bash
CREATE DATABASE postgre_db;
```

**OUTPUT:**
```bash
CREATE DATABASE
```

**INPUT:**
```bash
\l
```

**OUTPUT:**
```bash
                                             List of databases
   Name     | Owner | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider | Access privileges 
------------+-------+----------+------------+------------+------------+-----------------+-------------------
 postgre_db | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 postgres   | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 root       | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0  | root  | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/root          +
            |       |          |            |            |            |                 | root=CTc/root
```

**INPUT:**
```bash
\c postgre_db
```

**OUTPUT:**
```bash
You are now connected to database "postgre_db" as user "postgres".
```

To list tables run:

**INPUT:**
```bash
\dt
```

**OUTPUT:**
```bash
          List of relations
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | hero    | table | postgres
 public | student | table | postgres
(2 rows)
```

---

<div id="python-settings"></div>

## Settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
python -m venv sqlalchemy-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (WINDOWS):**  
```bash
source sqlalchemy-environment/Scripts/activate
```

**ACTIVATE THE VIRTUAL ENVIRONMENT (LINUX):**  
```bash
source sqlalchemy-environment/bin/activate
```

**UPDATE PIP:**
```bash
python -m pip install --upgrade pip
```

**INSTALL PYTHON DEPENDENCIES:**  
```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**Now, Be Happy!!!** 😬










<!--- ( References ) --->

---

<div id="references"></div>

## References

 - [Google Gemini](https://gemini.google.com/app)
 - [ChatGPT](https://chatgpt.com/)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
