# Select

## Contents

 - [Selecting Rows](#selecting-rows)
 - [Using WHERE clause](#where)

---

<div id="selecting-rows"></div>

## Mapping select query with "MetaTadaObject.select()"

To understand how it works, first, let's  remember what's MetaDataObject:

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

Here, the student is our MetaDataObject mapping. Now, we just need to import him and use select() method to generate a SELECT query for student table:

```python
from core_model import student

select_query = student.select()
print(select_query)
```

**OUTPUT:**  
```python
SELECT student.id, student.name, student.lastname 
FROM student
```

Now, we need run **execute()** method with the query:

```python
select_query = student.select()
s_result = conn.execute(select_query)
```

**Where's select result?**  
The result of the select is in the variable **"s_result"**:

```python
for row in s_result:
    print(row)
```

**OUTPUT:**  
```python
(1, 'Maria', 'Jose')
(2, 'João', 'Benedito')
(3, 'Herbet', 'Silva')
(4, 'Jhon', 'Allan')
(5, 'Mary', 'Key')
(6, 'Wesley', 'Lima')
```

---

<div id="where"></div>

## Using WHERE clause

The **WHERE** clause of **SELECT** query can be applied by using **select().where()**. For example, if we want to display rows with id >2:

```python
select_query = student.select().where(student.c.id > 3)
s_result = conn.execute(select_query)
for row in s_result:
    print(row)
```

**NOTE:**  
Here **c** attribute is an alias for **column**.

**OUTPUT:**  
```python
SELECT student.id, student.name, student.lastname 
FROM student 
WHERE student.id > %(id_1)s
2022-07-16 08:55:08,424 INFO sqlalchemy.engine.Engine [generated in 0.00024s] {'id_1': 3}
(4, 'Jhon', 'Allan')
(5, 'Mary', 'Key')
(6, 'Wesley', 'Lima')
```

---

**REFERENCES:**  
[SQLAlchemy Core - Selecting Rows](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_selecting_rows.htm)  

---

**Rodrigo Leite -** *drigols*
