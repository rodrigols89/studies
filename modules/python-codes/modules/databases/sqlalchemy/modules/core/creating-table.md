# Creating Tables

## Contents

 - [Creating a student table](#ex-01)
 - [Creating a generic create_table() function](#generic)

---

<div id="ex-01"></div>

## Creating a student table

To create a SQLAlchemy table first let's create a model:

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

**NOTE:**  
Now, we need use **create_all()** function from **MetaTada** object to create a table. The function **create_all()** receives an Engine object:

[core_model.py](src/core_model.py)
```python
from sqlalchemy import Table, Column, Integer, String, MetaData

from connections import get_engine_connection

studentMetaData = MetaData()

student = Table(
    'student', studentMetaData, 
    Column('id', Integer, primary_key = True), 
    Column('name', String(10)), 
    Column('lastname', String(10)), 
)

studentMetaData.create_all(get_engine_connection('root', 'toor', 'sqlalchemy-db'))
```

**OUTPUT:**  
```python
2022-07-15 05:53:12,763 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2022-07-15 05:53:12,763 INFO sqlalchemy.engine.Engine [raw sql] {}
2022-07-15 05:53:12,764 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
2022-07-15 05:53:12,764 INFO sqlalchemy.engine.Engine [raw sql] {}
2022-07-15 05:53:12,765 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
2022-07-15 05:53:12,765 INFO sqlalchemy.engine.Engine [raw sql] {}
2022-07-15 05:53:12,767 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-07-15 05:53:12,769 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2022-07-15 05:53:12,769 INFO sqlalchemy.engine.Engine [generated in 0.00021s] {'table_schema': 'sqlalchemy-db', 'table_name': 'student'}
2022-07-15 05:53:12,773 INFO sqlalchemy.engine.Engine 
CREATE TABLE student (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        name VARCHAR(10), 
        lastname VARCHAR(10), 
        PRIMARY KEY (id)
)


2022-07-15 05:53:12,773 INFO sqlalchemy.engine.Engine [no key 0.00023s] {}
2022-07-15 05:53:14,009 INFO sqlalchemy.engine.Engine COMMIT
```

> **NOTE:**  
> Because **echo** attribute of **create_engine()** function is set to **True**, the console will display the actual SQL query for table creation.

Another approach to create table from different model file is:

[core_test_drive.py](src/core_test_drive.py)
```python
from connections import get_engine_connection
from core_model import studentMetaData

engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')

studentMetaData.create_all(engine)
```

---

<div id="generic"></div>

## Creating a generic create_table() function

Now, we learn how create a generic function to create any table:

[create_table.py](src/create_table.py)
```python
def create_table(engine, medaDataModel):
    medaDataModel.create_all(engine)
```

Let's test:

[core_test_drive.py](src/core_test_drive.py)
```python
from core_model import studentMetaData

create_table(engine=engine, medaDataModel=studentMetaData)
```

**OUTPUT:**  
```python
2022-07-15 09:32:51,402 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-07-15 09:32:51,407 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2022-07-15 09:32:51,407 INFO sqlalchemy.engine.Engine [generated in 0.00060s] {'table_schema': 'sqlalchemy-db', 'table_name': 'student'}
2022-07-15 09:32:51,411 INFO sqlalchemy.engine.Engine 
CREATE TABLE student (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        name VARCHAR(10), 
        lastname VARCHAR(10), 
        PRIMARY KEY (id)
)


2022-07-15 09:32:51,411 INFO sqlalchemy.engine.Engine [no key 0.00020s] {}
2022-07-15 09:32:52,558 INFO sqlalchemy.engine.Engine COMMIT
```

See we have just a simple function that receives:

 - **An Engine**
 - **MetaData:**
   - MetaData class instance referent to your model Table().

---

**REFERENCES:**  
[SQLAlchemy Core - Creating Table](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm)  

---

**Rodrigo Leite -** *drigols*
