# Working with Engines and Connections

## Contents

 - [Getting Started](#getting-started)
 - [Working with Engine.begin() method](#engine-begin)

---

<div id="getting-started"></div>

## Getting Started

The most basic function of the Engine is to provide access to a Connection, which can then invoke SQL statements. To emit a textual statement to the database looks like:

```python
from sqlalchemy import text

from connections import get_engine_connection

engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')

with engine.connect() as conn:
    result = conn.execute(text("SELECT id, name, lastname FROM student"))
    for row in result:
        print(f"ID: {row['id']}, Name: {row['name']}, lastname: {row['lastname']}")
```

**OUTPUT:**
```python
ID: 1, Name: Maria, lastname: Jose
ID: 2, Name: João, lastname: Benedito
ID: 3, Name: Herbet, lastname: Silva
ID: 4, Name: Jhon, lastname: Allan
ID: 5, Name: Mary, lastname: Key
ID: 6, Name: Wesley, lastname: Lima
```

**NOTE:**  
Above, the **engine.connect()** method returns a **Connection object**, and by using it in a Python context manager **(e.g. the with: statement)** the **Connection.close()** method is automatically invoked at the end of the block.

---

<div id="engine-begin"></div>

## Working with .begin() method

> The **Connection** object provides a **Connection.begin()** method which <u>returns a Transaction object</u>.

Like the Connection itself, this object is usually used within a **Python with:** block so that its scope is managed:

**CODE:**  
```python
from connections import get_engine_connection
from core_model import student as student_tb

engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')

with engine.connect() as connection:
    with connection.begin():
        connection.execute(student_tb.insert(), {"name": "Edvaldo", "lastname": "Gomes"})
```

**NOTE:**  
The above block can be stated more simply by using the **Engine.begin()** method of **Engine**:

**CODE:**  
```python
from sqlalchemy import text

from connections import get_engine_connection
from core_model import student as student_tb

engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')

with engine.begin() as connection:
    connection.execute(student_tb.insert(), {"name": "Reginaldo", "Freire": "Gomes"})
```

If you test on database:

```python
SELECT * FROM student;

+----+-----------+----------+
| id | name      | lastname |
+----+-----------+----------+
|  1 | Maria     | Jose     |
|  2 | João      | Benedito |
|  3 | Herbet    | Silva    |
|  4 | Jhon      | Allan    |
|  5 | Mary      | Key      |
|  6 | Wesley    | Lima     |
|  7 | Edvaldo   | Gomes    |
|  8 | Reginaldo | NULL     |
+----+-----------+----------+
```

> **But, why I could use Engine.begin()?**

**NOTE:**  
 - The block managed by each **.begin()** method has the behavior such that the transaction is committed when the block completes.
 - If an exception is raised, the transaction is instead <u>rolled back</u>, and the exception propagated outwards.

**NOTE:**  
The underlying object used to represent the transaction is the **Transaction object**. This object is returned by the **Connection.begin()** method and includes the methods **Transaction.commit()** and **Transaction.rollback()**. The context manager calling form, which invokes these methods automatically, is recommended as a best practice.

---

**REFERENCES:**  
[Working with Engines and Connections](https://docs.sqlalchemy.org/en/14/core/connections.html)  

---

**Rodrigo Leite -** *drigols*
