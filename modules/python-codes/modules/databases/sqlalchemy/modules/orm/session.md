# Session

## Contents

 - [Intro to SQLAlchemy Session](#intro)

---

<div id="intro"></div>

## Intro to SQLAlchemy Session

**NOTE:**  
In order to interact with the database, we need to obtain its handle.

> A <u>session object</u> is the handle to database.

To create a SQLAlchemy session is very simple:

[connections.py](src/connections.py)
```python
from sqlalchemy.orm import sessionmaker

def get_session(engine):
    Session = sessionmaker(bind = engine)
    return Session
```

**NOTE:**  
Some of the frequently required methods of session class are listed below:

| Method           | Description
|------------------|--------------------------------------------------------------------------------------------------
| **begin()**      | Begins a transaction on this session.
| **add()**        | Places an object in the session. Its state is persisted in the database on next flush operation.
| **add_all()**    | Adds a collection of objects to the session.
| **commit()**     | Flushes all items and any transaction in progress.
| **delete()**     | Marks a transaction as deleted.
| **execute()**    | Executes a SQL expression.
| **expire()**     | Marks attributes of an instance as out of date.
| **flush()**      | Flushes all object changes to the database.
| **invalidate()** | Closes the session using connection invalidation.
| **rollback()**   | Rolls back the current transaction in progress. 
| **close()**      | Closes current session by clearing all items and ending any transaction in progress.

---

**REFERENCES:**  
[SQLAlchemy ORM - Creating Session](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_creating_session.htm)  

---

**Rodrigo Leite -** *drigols*
