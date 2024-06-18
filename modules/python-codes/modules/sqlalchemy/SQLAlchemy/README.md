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
