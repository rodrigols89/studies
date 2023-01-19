# Engine Configuration

## Contents

 - [Intro to Engine](#intro)
 - [Engine Creation API](#create-api)
 - [Function create_engine()](#create-engine)
 - [create_engine() methods](#create-engine-methods)

---

<div id="intro"></div>

## Intro to Engine

The **[Engine](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine)** is the starting point for any SQLAlchemy application. It’s “home base” for the actual database and its DBAPI, delivered to the SQLAlchemy application through a connection pool and a Dialect, which describes how to talk to a specific kind of database/DBAPI combination.

The general structure can be illustrated as follows:

![img](images/sqla_engine_arch.png)  

---

<div id="create-api"></div>

## Engine Creation API

The most common API for create Engine are:

| Object Name	                                        | Description                                                      |
|-------------------------------------------------------|------------------------------------------------------------------|
| create_engine(url, **kwargs)                          | Create a new Engine instance.                                    |
| create_mock_engine(url, executor, **kw)               | Create a “mock” engine used for echoing DDL.                     |
| engine_from_config(configuration[, prefix], **kwargs) | Create a new Engine instance using a configuration dictionary.   |
| make_url(name_or_url)                                 | Given a string or unicode instance, produce a new URL instance.  |
| URL                                                   | Represent the components of a URL used to connect to a database. |

---

<div id="create-engine"></div>

## Function create_engine()

An **Engine** object is instantiated publicly using the **[create_engine()](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine)** function:

**Database URLs:**  
The **[create_engine()](https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine)** function produces an Engine object based on a URL. These URLs follow RFC-1738, and usually can include:

 - username;
 - password;
 - hostname;
 - database name...

As well as optional keyword arguments for additional configuration. In some cases a file path is accepted, and in others a “data source name” replaces the “host” and “database” portions. The typical form of a database URL is:

```python
dialect+driver://username:password@host:port/database
```

 - **dialect:**
   - *Dialect* names include the identifying name of the SQLAlchemy dialect, a name such as <u>sqlite</u>, <u>mysql</u>, <u>postgresql</u>, <u>oracle</u>, or <u>mssql</u>.
 - **driver:**
   - The *drivername* is the name of the DBAPI to be used to connect to the database using all lowercase letters:
     - If not specified, a “default” DBAPI will be imported if available - this default is typically the most widely known driver available for that backend.

To create a SQLAlchemy connection is very simple, imagine you have the function to get a connection, like it:

[connections.py](src/connections.py)
```python
def get_engine_connection(
    username, password, database, host="localhost", port="3306"
):
    try:
        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
            echo=True,
        )
        return engine
    except Exception as error:
        print(error)
```

Now, let's test:

[test_drive.py](src/test_drive.py)
```python
from connections import get_engine_connection


if __name__ == '__main__':

    # Testing connection.
    print('\nTesting connection:')
    engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')
    print(engine)
    print(type(engine))
    print(bool(engine))
```

**OUTPUT:**  
```python
Testing connection:
Engine(mysql+pymysql://root:***@localhost:3306/sqlalchemy-db)
<class 'sqlalchemy.engine.base.Engine'>
True
```

**NOTE:**  
The **echo flag** is a shortcut to set up SQLAlchemy logging, which is accomplished via Python’s standard logging module. To hide the verbose output, set echo attribute to **None**.

---

<div id="create-engine-methods"></div>

## create_engine() methods

> The **create_engine()** function <u>returns an Engine object</u>.

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

**REFERENCES**  
[SQLAlchemy Core - Connecting to Database](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_connecting_to_database.htm)  
[Engine Configuration](https://docs.sqlalchemy.org/en/14/core/engines.html)  

---

**Rodrigo Leite -** *drigols*
