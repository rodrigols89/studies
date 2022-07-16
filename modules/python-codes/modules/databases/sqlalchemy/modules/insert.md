# Inserting Data

## Contents

 - [Creating inserts with the MetaDataObject.insert().values() methods](#creating-inserts)
 - [Inserting Data from Lists and Dictionaries](#lists-dictionaries)

---

<div id="creating-inserts"></div>

## Creating inserts with the MetaDataObject.insert().values() methods

> **NOTE:**  
> In order to execute the resulting SQL expressions, we have to obtain a connection object representing an actively checked out DBAPI connection resource and then feed the expression object as shown in the code below.

Like it:

```python
conn = engine.connect()
```

To understand how it works, first let's see a table created with MetaData mapping:

[core_model.py](src/core_model.py)
```python
from sqlalchemy import Table, Column, Integer, String, MetaData

studentMetaData = MetaData()

student = Table(
    'student', studentMetaData, 
    Column('id', Integer, primary_key = True), 
    Column('name', String(10)), 
    Column('lastname', String(10)), 
)
```

The **student** object is a MetaData object; Now just we need is create a mapping for our object student and our Database table with the **insert().values()** methods:

[core_test_drive.py](src/core_test_drive.py)
```python
ins = student.insert().values(name = 'Rodrigo', lastname = 'Leite')
print(ins)
```

**OUTPUT:**  
```python
INSERT INTO student (name, lastname) VALUES (:name, :lastname)
```

**NOTE:**  
For now, we just have a mapping to insert data into table student, to insert we need first get a connection create by:

```python
conn = engine.connect()
```

Next, insert data with method **execute()**:

```python
conn = engine.connect()

ins = student.insert().values(name = 'Rodrigo', lastname = 'Leite')
conn.execute(ins)
```

To check, go to Database and enter:

```python
SELECT * FROM student;
```

**OUTPUT:**  
```python
+----+---------+----------+
| id | name    | lastname |
+----+---------+----------+
|  1 | Rodrigo | Leite    |
+----+---------+----------+
1 row in set (0.00 sec)
```

---

<div id="lists-dictionaries"></div>

## Inserting Data from Lists and Dictionaries

We can also pass **lists** and **dictionaries** to **insert().values()** methods to mapping, and next insert with the **execute()** method:

**List example:**  
```python
student_list = [
    {
        'name': 'Maria',
        'lastname': 'Jose'
    },
    {
        'name': 'João',
        'lastname': 'Benedito'
    },
    {
        'name': 'Herbet',
        'lastname': 'Silva'
    },
    {
        'name': 'Jhon',
        'lastname': 'Allan'
    },
    {
        'name': 'Mary',
        'lastname': 'Key'
    },
    {
        'name': 'Wesley',
        'lastname': 'Lima'
    }
]

ins = student.insert().values(student_dict)
conn.execute(ins)
```

To check, go to Database and enter:

```python
SELECT * FROM student;
```

**OUTPUT:**  
```python
+----+---------+----------+
| id | name    | lastname |
+----+---------+----------+
|  1 | Rodrigo | Leite    |
|  2 | Maria   | Jose     |
|  3 | João    | Benedito |
|  4 | Herbet  | Silva    |
|  5 | Jhon    | Allan    |
|  6 | Mary    | Key      |
|  7 | Wesley  | Lima     |
+----+---------+----------+
```

**NOTE:**  
You can also pass object student.insert() with a list "student_list" to execute() method:

```python
conn.execute(student.insert(), student_list)
```

---

**REFERENCES:**  
[SQLAlchemy Core - Executing Expression](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_executing_expression.htm)  

---

**Rodrigo Leite -** *drigols*
