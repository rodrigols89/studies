# SQLAlchemy

## Contents

 - **General:**
   - [create_engine() object](#create-engine)
     - **Engine Object methods:**
       - [connect():](#engine-connect)
         - **Connect() object methods:**
           - [engine.connect().execute()](#engine-connect-execute)
           - [engine.connect().begin()](#engine-connect-begin)
   - [Session](#session)
 - **CRUD (CREATE, READ, UPDATE, DELETE):**
   - **CREATE:**
     - [create_all() method | Creating tables](#create-all)
     - [session.add(object) | Inserting data into a table](#session-add)
     - [session.add_all(data) | Inserting many registers](#session-add-all)
   - **READ:**
     - [SELECT using session.query(object)](#session-query)
   - **UPDATE:**
   - **DELETE:**
 - **Settings:**
   - [Docker composes](#settings-docker-composes)
   - [Python settings](#python-settings)
 - [**References**](#references)

<!--- ( General ) --->

---

<div id="create-engine"></div>

## create_engine() object

**Database URLs:**  
The **[create_engine()](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine)** function produces an Engine object based on a URL. These URLs follow RFC-1738, and usually can include:

 - username;
 - password;
 - hostname;
 - database name...

```python
dialect+driver://username:password@host:port/database
```

 - **dialect:**
   - *Dialect* names include the identifying name of the SQLAlchemy dialect, a name such as **sqlite**, **mysql**, **postgresql**, **oracle**, or **mssql**.
 - **driver:**
   - The *drivername* is the name of the DBAPI to be used to connect to the database using all lowercase letters:
     - If not specified, a “default” DBAPI will be imported if available - this default is typically the most widely known driver available for that backend.

To create a SQLAlchemy connection is very simple, imagine you have the function to get a engine, like it:

**MySQL example:**
[driver_engine.py](src/mysql/driver_engine.py)
```python
from sqlalchemy import create_engine


def get_engine_connection(
    username, password, database, host="localhost", port="3310"
):
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
    except Exception as e:
        print("An error occurred while the Engine initializing:", str(e))
    else:
        return engine

if __name__ == "__main__":

    # Database settings
    username = "root"
    password = "toor"
    database = "mysql-db"

    print("================= ( Database Engine ) ==================")
    engine = get_engine_connection(username, password, database)
    print(engine)
    print("type = ", type(engine))
    print("bool = ", bool(engine))
```

**OUTPUT:**  
```python
================= ( Database Engine ) ==================
Engine(mysql+pymysql://root:***@localhost:3310/mysql-db)
type =  <class 'sqlalchemy.engine.base.Engine'>
bool =  True
```

**NOTE:**  
The **echo flag** is a shortcut to set up SQLAlchemy logging, which is accomplished via Python’s standard logging module. To hide the verbose output, set echo attribute to **False/None**.

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_engine.py](src/postgresql/driver_engine.py)
```python
from sqlalchemy import create_engine


def get_engine_connection(
    username, password, database, host="localhost", port="5432"
):
    try:
        engine = create_engine(
            f"postgresql://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
    except Exception as e:
        print("An error occurred while the Engine initializing:", str(e))
    else:
        return engine

if __name__ == "__main__":

    # Database settings
    username = "postgres"
    password = "toor"
    database = "postgre_db"

    print("================= ( Database Engine ) ==================")
    engine = get_engine_connection(username, password, database)
    print(engine)
    print("type = ", type(engine))
    print("bool = ", bool(engine))
```

**INPUT:**  
```bash
python driver_engine.py 
```

**OUTPUT:**  
```bash
================= ( Database Engine ) ==================
Engine(postgresql://postgres:***@localhost:5432/postgre_db)
type =  <class 'sqlalchemy.engine.base.Engine'>
bool =  True
```

---

<div id="create-engine-methods"></div>

## create_engine() methods

> The **create_engine()** function *returns an Engine object*.

Some important methods of Engine class are:

| Method            |  Description
|-------------------|--------------------------------------
| **connect()**     | Returns connection object
| **execute()**     | Executes a SQL statement construct
| **begin()**       | Returns a context manager delivering a Connection with a Transaction established. Upon successful operation, the Transaction is committed, else it is rolled back
| **dispose()**     | Disposes of the connection pool used by the Engine 
| **driver()**      | Driver name of the Dialect in use by the Engine
| **table_names()** | Returns a list of all table names available in the database
| **transaction()** | Executes the given function within a transaction boundary

---

<div id="engine-connect"></div>

## connect()

> The **engine.connect() method** is used to establish a connection to the database. It returns a **connection object (Connection)** that allows executing queries and transactions on the database.

Here, are some Connection object Methods and attributes:

 - **Methods:**
   - **execute(query, `*multiparams`, `**params`):**
     - Executes a SQL query on the database. You can pass a string containing the SQL query and optionally additional parameters.
   - **execute(text(query), `**params`):**
     - Executes a SQL query using a textual expression. This is useful when you need to execute dynamic SQL queries with substituted values.
   - **execute(stmt, `*multiparams`, `**params`):**
     - Executes a Statement object or an SQLAlchemy SQL expression. This allows executing more complex or pre-compiled queries.
   - **execute(script) or execute(script1, script2, ...):**
     - Executes one or more Script objects to execute SQL commands and scripts.
 - **Attributes:**
   - **closed:**
     - Indicates whether the connection is closed (True) or open (False).
   - **connection:**
     - Returns the underlying connection object used by the underlying database library (e.g., psycopg2, mysql-connector, etc.). This can be useful if you need to access specific methods of the database adapter.
   - **engine:**
     - Returns the Engine object associated with the connection.

---

<div id="engine-connect-execute"></div>

##  engine.connect().execute()

> The **execute() method** is used to execute an SQL query on the database. It sends the query to the database through the connection associated with the Engine object and returns a **ResultProxy** *object* that contains the query results.

For example, seee the code below:

**MySQL example:**
[driver_execute.py](src/mysql/driver_execute.py)
```python
result = engine.connect().execute(text("SELECT * FROM student"))
for row in result:
    print(f"ID: {row[0]}, Name: {row[1]}, lastname: {row[2]}")
```

**NOTE:**  
You can format the code to use the **"with"** and **"try..except"** statements:

**MySQL example:**
[driver_execute.py](src/mysql/driver_execute.py)
```python
try:
    with engine.connect() as connection:
        try:
            result = connection.execute(text("SELECT * FROM student"))
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, lastname: {row[2]}")
        except Exception as e:
            print("An error occurred during the SELECT (connection.execute) operation:", str(e))
except Exception as e:
    print("An error occurred to initialize the Connection object:", str(e))
```

**INTPUT:**
```bash
python driver_execute.py
```

**OUTPUT:**
```bash
ID: 1, Name: John, lastname: Doe
ID: 2, Name: Jane, lastname: Smith
ID: 3, Name: Rodrigo, lastname: Leite
ID: 4, Name: Ricardo, lastname: Bruno
ID: 5, Name: Mary, lastname: Jane
ID: 6, Name: Richard, lastname: Belmont
ID: 7, Name: Isaac, lastname: Newton
ID: 8, Name: Lionel, lastname: Messi
ID: 9, Name: Cristiano, lastname: Ronaldo
ID: 10, Name: Jesus, lastname: Cristo
```

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_execute.py](src/postgresql/driver_execute.py)
```python
from sqlalchemy import create_engine, text


# Database settings
username = "postgres"
password = "toor"
database = "postgre_db"
host="localhost"
port="5432"
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

try:
    with engine.connect() as connection:
        try:
            result = connection.execute(text("SELECT * FROM student"))
            for row in result:
                print(f"ID: {row[0]}, Name: {row[1]}, lastname: {row[2]}")
        except Exception as e:
            print("An error occurred during the SELECT (connection.execute) operation:", str(e))
except Exception as e:
    print("An error occurred to initialize the Connection object:", str(e))
```

**INTPUT:**
```bash
python driver_execute.py
```

**OUTPUT:**
```bash
ID: 1, Name: John, lastname: Doe
ID: 2, Name: Jane, lastname: Smith
ID: 3, Name: Rodrigo, lastname: Leite
ID: 4, Name: Ricardo, lastname: Bruno
ID: 5, Name: Mary, lastname: Jane
ID: 6, Name: Richard, lastname: Belmont
ID: 7, Name: Isaac, lastname: Newton
ID: 8, Name: Lionel, lastname: Messi
ID: 9, Name: Cristiano, lastname: Ronaldo
ID: 10, Name: Jesus, lastname: Cristo
```

---

<div id="engine-connect-begin"></div>

## engine.connect().begin()

The **begin() method** is used to start a transaction in the database. A transaction allows grouping multiple database operations as a single atomic unit. You can execute multiple queries and either **commit (commit())** or **rollback (rollback())** the changes made to the database.

For example, see the code below:

**MySQL example:**
[driver_begin.py](src/mysql/driver_begin.py)
```python
connection  = engine.connect()
transaction = connection.begin() # Start a transaction.
connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Will', 'Smith')"))
connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Margot', 'Robbie')"))
transaction.commit()
connection.close()
```

**NOTE:**  
You can format the code to use the **"with"** and **"try..except"** statements:

**MySQL example:**
[driver_begin.py](src/mysql/driver_begin.py)
```python
try:
    with engine.connect() as connection:
        try:
            transaction = connection.begin()
            connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Will', 'Smith')"))
            connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Margot', 'Robbie')"))
            transaction.commit()  # Commit the changes.
            print("Operation completed successfully!")
        except Exception as e:
            transaction.rollback()
            print("An error occurred during the INSERT INTO (connection.execute) operation:", str(e))
except Exception as e:
    print("An error occurred to initialize the Connection object:", str(e))
```

**INTPUT:**
```bash
python driver_begin.py
```

**OUTPUT:**
```bash
Operation completed successfully!
```

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_begin.py](src/postgresql/driver_begin.py)
```python
try:
    with engine.connect() as connection:
        try:
            transaction = connection.begin()
            connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Will', 'Smith')"))
            connection.execute(text("INSERT INTO student (name, lastname) VALUES ('Margot', 'Robbie')"))
            transaction.commit()  # Commit the changes.
            print("Operation completed successfully!")
        except Exception as e:
            transaction.rollback()
            print("An error occurred during the INSERT INTO (connection.execute) operation:", str(e))
except Exception as e:
    print("An error occurred to initialize the Connection object:", str(e))
```

**INTPUT:**
```bash
python driver_begin.py
```

**OUTPUT:**
```bash
Operation completed successfully!
```

<!--- ( Session ) --->

---

<div id="session"></div>

## Session

> A session object is the handle (identificador) to database.

Session class is defined using **sessionmaker()**:

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
```

The session object is then set up using its default constructor as follows:

```python
session = Session()
```

Or using **"with"** statement:

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

<!--- ( CREATE ) --->

---

<div id="create-all"></div>

## create_all() method | Creating tables

> The **create_all() method** is used to create all tables stored in **MetaData (or declarative_base)**.

For example, image we have to class model to represent **Heroes**, and **Students**:

**MySQL example:**
[driver_models.py](src/mysql/driver_models.py)
```python
from sqlalchemy import Column, Float, Integer, VARCHAR
from sqlalchemy import create_engine
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

**MySQL example:**
[driver_models.py](src/mysql/driver_models.py)
```python
if __name__ == "__main__":
    
    # Database settings
    username = "root"
    password = "toor"
    database = "mysql-db"
    host="localhost"
    port="3310"

    # Make an Engine.    
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
        echo=True,
    )

    Base.metadata.create_all(engine)
    print ('\nTable created on database')
```

**INPUT:**  
```bash
python driver_models.py
```

**OUTPUT:**  
```bash
2023-05-19 01:47:43,334 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2023-05-19 01:47:43,334 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-19 01:47:43,335 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
2023-05-19 01:47:43,335 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-19 01:47:43,335 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
2023-05-19 01:47:43,335 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-19 01:47:43,336 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-05-19 01:47:43,336 INFO sqlalchemy.engine.Engine DESCRIBE `mysql-db`.`hero`
2023-05-19 01:47:43,336 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-19 01:47:43,337 INFO sqlalchemy.engine.Engine DESCRIBE `mysql-db`.`student`
2023-05-19 01:47:43,337 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-19 01:47:43,339 INFO sqlalchemy.engine.Engine 
CREATE TABLE hero (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        name VARCHAR(50) NOT NULL, 
        npc_name VARCHAR(50) NOT NULL, 
        primary_attr VARCHAR(50) NOT NULL, 
        attack_type VARCHAR(50) NOT NULL, 
        img VARCHAR(100) NOT NULL, 
        icon VARCHAR(100) NOT NULL, 
        base_health FLOAT NOT NULL, 
        base_health_regen FLOAT NOT NULL, 
        base_mana FLOAT NOT NULL, 
        base_mana_regen FLOAT NOT NULL, 
        base_armor FLOAT NOT NULL, 
        base_attack_min FLOAT NOT NULL, 
        base_attack_max FLOAT NOT NULL, 
        base_str FLOAT NOT NULL, 
        base_agi FLOAT NOT NULL, 
        base_int FLOAT NOT NULL, 
        str_gain FLOAT NOT NULL, 
        agi_gain FLOAT NOT NULL, 
        int_gain FLOAT NOT NULL, 
        attack_range FLOAT NOT NULL, 
        projectile_speed FLOAT NOT NULL, 
        move_speed FLOAT NOT NULL, 
        legs INTEGER NOT NULL, 
        PRIMARY KEY (id)
)


2023-05-19 01:47:43,339 INFO sqlalchemy.engine.Engine [no key 0.00008s] {}
2023-05-19 01:47:43,360 INFO sqlalchemy.engine.Engine 
CREATE TABLE student (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        name VARCHAR(50) NOT NULL, 
        lastname VARCHAR(50) NOT NULL, 
        PRIMARY KEY (id)
)


2023-05-19 01:47:43,360 INFO sqlalchemy.engine.Engine [no key 0.00008s] {}
2023-05-19 01:47:43,371 INFO sqlalchemy.engine.Engine COMMIT
```

> **NOTE:**  
> How the **"echo"** attribute of **"create_engine()"** function was set as **True**, the console will display the SQL query for table creation.

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_models.py](src/postgresql/driver_models.py)
```python
from sqlalchemy import Column, Float, Integer, VARCHAR
from sqlalchemy import create_engine
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


if __name__ == "__main__":
    
    # Database settings
    username = "postgres"
    password = "toor"
    database = "postgre_db"
    host="localhost"
    port="5432"

    # Make an Engine.    
    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{database}",
        echo=True,
    )

    Base.metadata.create_all(engine)
```

**INTPUT:**
```bash
python driver_models.py 
```

**OUTPUT:**
```bash
2023-05-21 01:38:05,160 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2023-05-21 01:38:05,160 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-21 01:38:05,161 INFO sqlalchemy.engine.Engine select current_schema()
2023-05-21 01:38:05,161 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-21 01:38:05,161 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2023-05-21 01:38:05,161 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-05-21 01:38:05,162 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-05-21 01:38:05,164 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2023-05-21 01:38:05,164 INFO sqlalchemy.engine.Engine [generated in 0.00014s] {'table_name': 'hero', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2023-05-21 01:38:05,165 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2023-05-21 01:38:05,165 INFO sqlalchemy.engine.Engine [cached since 0.001352s ago] {'table_name': 'student', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2023-05-21 01:38:05,166 INFO sqlalchemy.engine.Engine 
CREATE TABLE hero (
        id SERIAL NOT NULL, 
        name VARCHAR(50) NOT NULL, 
        npc_name VARCHAR(50) NOT NULL, 
        primary_attr VARCHAR(50) NOT NULL, 
        attack_type VARCHAR(50) NOT NULL, 
        img VARCHAR(100) NOT NULL, 
        icon VARCHAR(100) NOT NULL, 
        base_health FLOAT NOT NULL, 
        base_health_regen FLOAT NOT NULL, 
        base_mana FLOAT NOT NULL, 
        base_mana_regen FLOAT NOT NULL, 
        base_armor FLOAT NOT NULL, 
        base_attack_min FLOAT NOT NULL, 
        base_attack_max FLOAT NOT NULL, 
        base_str FLOAT NOT NULL, 
        base_agi FLOAT NOT NULL, 
        base_int FLOAT NOT NULL, 
        str_gain FLOAT NOT NULL, 
        agi_gain FLOAT NOT NULL, 
        int_gain FLOAT NOT NULL, 
        attack_range FLOAT NOT NULL, 
        projectile_speed FLOAT NOT NULL, 
        move_speed FLOAT NOT NULL, 
        legs INTEGER NOT NULL, 
        PRIMARY KEY (id)
)


2023-05-21 01:38:05,166 INFO sqlalchemy.engine.Engine [no key 0.00008s] {}
2023-05-21 01:38:05,170 INFO sqlalchemy.engine.Engine 
CREATE TABLE student (
        id SERIAL NOT NULL, 
        name VARCHAR(50) NOT NULL, 
        lastname VARCHAR(50) NOT NULL, 
        PRIMARY KEY (id)
)


2023-05-21 01:38:05,171 INFO sqlalchemy.engine.Engine [no key 0.00041s] {}
2023-05-21 01:38:05,173 INFO sqlalchemy.engine.Engine COMMIT
```

---

<div id="session-add"></div>

## session.add(object) | Inserting data into a table

> An approach to insert data into a table is used **session.add(object)** method.

For example, let's pass an object with values to the **session.add(object)** method:

**MySQL example:**
[driver_insert.py](src/mysql/driver_insert.py)
```python
# Create an object (instance) student.
student = StudentModel(name='John', lastname='Doe')

try:
    with Session(engine) as session:
        try:
            session.add(student)
            session.commit()
            print("Insert (add) operation completed successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred during the insert (add) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
```

**NOTE:**  
In this code, we assume that the operation was successful if no exception is raised during the *commit*. If an exception occurs, we roll back the transaction using **"session.rollback()"** to ensure data integrity.

**INTPUT:**
```bash
python driver_insert.py
```

**OUTPUT:**
```bash
Insert (add) operation completed successfully!
```

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_insert.py](src/postgresql/driver_insert.py)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from driver_models import StudentModel


# Database settings
username = "postgres"
password = "toor"
database = "postgre_db"
host="localhost"
port="5432"
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

# Create an object (instance) student.
student = StudentModel(name='John', lastname='Doe')

try:
    with Session(engine) as session:
        try:
            session.add(student)
            session.commit()
            print("Insert (add) operation completed successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred during the insert (add) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
```

**INTPUT:**
```bash
python driver_insert.py
```

**OUTPUT:**
```bash
Insert (add) operation completed successfully!
```

---

<div id="session-add-all"></div>

## session.add_all(data) | Inserting many registers

We also can use the **session.add_all(data) method** to insert many registers at the same time:

**MySQL example:**
[driver_add_all.py](src/mysql/driver_add_all.py)
```python
data = [
    {"name": "John", "lastname": "Doe"},
    {"name": "Jane", "lastname": "Smith"},
    {"name": "Rodrigo", "lastname": "Leite"},
    {"name": "Ricardo", "lastname": "Bruno"},
    {"name": "Mary", "lastname": "Jane"},
    {"name": "Richard", "lastname": "Belmont"},
    {"name": "Isaac", "lastname": "Newton"},
    {"name": "Lionel", "lastname": "Messi"},
    {"name": "Cristiano", "lastname": "Ronaldo"},
    {"name": "Jesus", "lastname": "Cristo"},
]
students = [StudentModel(name=item["name"], lastname=item["lastname"]) for item in data]

try:
    with Session(engine) as session:
        try:
            session.add_all(students)
            session.commit()
            print("Insert (add_all) operation completed successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred during the insert (add_all) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
```

**NOTE:**  
In this example:

 - we have a list **data** that contains the attribute values **"name"** and **"lastname"** for each record.
 - Then use a **list comprehension** to create a *list of StudentModel objects* based on the dictionary values.

**INTPUT:**
```bash
python driver_add_all.py
```

**OUTPUT:**
```bash
Insert (add_all) operation completed successfully!
```

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_add_all.py](src/postgresql/driver_add_all.py)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from driver_models import StudentModel


# Database settings
username = "postgres"
password = "toor"
database = "postgre_db"
host="localhost"
port="5432"
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

data = [
    {"name": "John", "lastname": "Doe"},
    {"name": "Jane", "lastname": "Smith"},
    {"name": "Rodrigo", "lastname": "Leite"},
    {"name": "Ricardo", "lastname": "Bruno"},
    {"name": "Mary", "lastname": "Jane"},
    {"name": "Richard", "lastname": "Belmont"},
    {"name": "Isaac", "lastname": "Newton"},
    {"name": "Lionel", "lastname": "Messi"},
    {"name": "Cristiano", "lastname": "Ronaldo"},
    {"name": "Jesus", "lastname": "Cristo"},
]
students = [StudentModel(name=item["name"], lastname=item["lastname"]) for item in data]

try:
    with Session(engine) as session:
        try:
            session.add_all(students)
            session.commit()
            print("Insert (add_all) operation completed successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred during the insert (add_all) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
```

**INTPUT:**
```bash
python driver_add_all.py
```

**OUTPUT:**
```bash
Insert (add_all) operation completed successfully!
```

<!--- ( READ ) --->

---

<div id="session-query"></div>

## SELECT using session.query(object)

> An approach to apply **SELECT** *statement* to a table is to use **session.query(object) method**.

For example, see the code below:

**MySQL example:**
[driver_session_query.py](src/mysql/driver_session_query.py)
```python
try:
    with Session(engine) as session:
        try:
            # Example 1: Select all students
            students = session.query(StudentModel).all()
            print("============================= ( SELECT ALL ) =============================")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")

            # Example 2: Select students based on specific criteria
            students = session.query(StudentModel).filter_by(name='Rodrigo', lastname='Leite').all()
            print("===== ( SELECT WHERE (.filter_by) name='Rodrigo' AND lastname='Doe' ) =====")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")

            # Example 3: Select only one student based on ID
            student = session.query(StudentModel).filter(StudentModel.id == 10).first()
            print("===== ( SELECT WHERE (.filter_by) (StudentModel.id == 1).first() ) ========")
            if student:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")
            else:
                print("Student not found.")
        except Exception as e:
            print("An error occurred during the SELECT (session.query) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
```

**INTPUT:**
```bash
python driver_session_query.py
```

**OUTPUT:**
```bash
============================= ( SELECT ALL ) =============================
ID: 1, Name: John, Lastname: Doe
ID: 2, Name: Jane, Lastname: Smith
ID: 3, Name: Rodrigo, Lastname: Leite
ID: 4, Name: Ricardo, Lastname: Bruno
ID: 5, Name: Mary, Lastname: Jane
ID: 6, Name: Richard, Lastname: Belmont
ID: 7, Name: Isaac, Lastname: Newton
ID: 8, Name: Lionel, Lastname: Messi
ID: 9, Name: Cristiano, Lastname: Ronaldo
ID: 10, Name: Jesus, Lastname: Cristo
===== ( SELECT WHERE (.filter_by) name='Rodrigo' AND lastname='Doe' ) =====
ID: 3, Name: Rodrigo, Lastname: Leite
===== ( SELECT WHERE (.filter_by) (StudentModel.id == 1).first() ) ========
ID: 10, Name: Jesus, Lastname: Cristo
```

Now, let's see the same example using **PostgreSQL** database:

**PostgreSQL example:**
[driver_session_query.py](src/postgresql/driver_session_query.py)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from driver_models import StudentModel


# Database settings
username = "postgres"
password = "toor"
database = "postgre_db"
host="localhost"
port="5432"
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

try:
    with Session(engine) as session:
        try:
            # Example 1: Select all students
            students = session.query(StudentModel).all()
            print("============================= ( SELECT ALL ) =============================")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")

            # Example 2: Select students based on specific criteria
            students = session.query(StudentModel).filter_by(name='Rodrigo', lastname='Leite').all()
            print("===== ( SELECT WHERE (.filter_by) name='Rodrigo' AND lastname='Doe' ) =====")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")

            # Example 3: Select only one student based on ID
            student = session.query(StudentModel).filter(StudentModel.id == 10).first()
            print("===== ( SELECT WHERE (.filter_by) (StudentModel.id == 1).first() ) ========")
            if student:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")
            else:
                print("Student not found.")
        except Exception as e:
            print("An error occurred during the SELECT (session.query) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
```

**INTPUT:**
```bash
python driver_session_query.py
```

**OUTPUT:**
```bash
============================= ( SELECT ALL ) =============================
ID: 1, Name: John, Lastname: Doe
ID: 2, Name: Jane, Lastname: Smith
ID: 3, Name: Rodrigo, Lastname: Leite
ID: 4, Name: Ricardo, Lastname: Bruno
ID: 5, Name: Mary, Lastname: Jane
ID: 6, Name: Richard, Lastname: Belmont
ID: 7, Name: Isaac, Lastname: Newton
ID: 8, Name: Lionel, Lastname: Messi
ID: 9, Name: Cristiano, Lastname: Ronaldo
ID: 10, Name: Jesus, Lastname: Cristo
===== ( SELECT WHERE (.filter_by) name='Rodrigo' AND lastname='Doe' ) =====
ID: 3, Name: Rodrigo, Lastname: Leite
===== ( SELECT WHERE (.filter_by) (StudentModel.id == 1).first() ) ========
ID: 10, Name: Jesus, Lastname: Cristo
```

<!--- ( Settings/Docker composes ) --->

---

<div id="settings-docker-composes"></div>

## Docker composes (MySQL, PostgreSQL)

### MySQL Docker Compose

```bash
sudo docker compose --file composes/mysql-docker-compose.yml up -d
```

```bash
sudo docker exec -it mysql-container bash
```

```bash
mysql --user=root --password=toor mysql-db
```

### PostgreSQL Docker Compose

```bash
sudo docker compose --file composes/postgresql-docker-compose.yml up -d
```

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

<!--- ( Settings/Python ) --->

---

<div id="python-settings"></div>

## Python settings

**CREATE VIRTUAL ENVIRONMENT:**  
```bash
# Venv approach.
python -m venv sqlalchemy-environment
```

**ACTIVATE THE VIRTUAL ENVIRONMENT:**  
```bash
# Linux approach
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

<!--- ( References ) --->

---

<div id="references"></div>

## References

 - [ChatGPT](#)
 - [SQLAlchemy Core - Connecting to Database](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.htm)
 - [Engine Configuration](https://docs.sqlalchemy.org/en/14/core/engines.html)  
 - [create_all](https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.MetaData.create_all)
 - [SQLAlchemy Core - Creating Table](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm)
 - [Working with Engines and Connections](https://docs.sqlalchemy.org/en/14/core/connections.html)

---

Ro**drigo** **L**eite da **S**ilva - **drigols**
