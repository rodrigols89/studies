# Criando Tabelas

## Contents

 - [01 - Criando Tabelas (create table) em um servidor MySQL em Python](#create-table)
 - [02 - Criando tabelas a partir de scripts prontos](#script)

---

<div id="create-table"></div>

## 01 - Criando Tabelas (create table) em um servidor MySQL em Python

Para criar tabelas em um **servidor MySQL** em Python é muito simples. Por exemplo, vejam o código abaixo:

```python
import mysql.connector

Laptop_tb = """
  CREATE TABLE Laptop (
    Id int(11) NOT NULL,
    Name varchar(250) NOT NULL,
    Price float NOT NULL,
    Purchase_date Date NOT NULL,
    PRIMARY KEY (Id)
  )
"""


try:
  connection = mysql.connector.connect(
    host='localhost',
    database='Electronics',
    user='root',
    password='toor'
  )
except mysql.connector.Error as error:
  print("Failed to create table in MySQL: {}".format(error))
else:
  cursor = connection.cursor()
  result = cursor.execute(Laptop_tb)
  print("Laptop Table created successfully!")
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed.")
```

**OUTPUT:**  
```python
Laptop Table created successfully!
MySQL connection is closed.
```

---

<div id="script"></div>

## 02 - Criando tabelas a partir de scripts prontos

As vezes é necessário criar várias tabelas no mesmo Banco de Dados. Sabendo disso, é interessante ter um **arquivo.py** que é responsável apenas por armazenar essas criações de tabelas e na hora que precisa só importar.

Por exemplo, vejam um **arquivo.py** responsável por criar tabelas e lá nós vamos salvar nossa criação da tabela laptop:

[create_table.py](src/sql/create_table.py)
```python
Laptop_tb = """
  CREATE TABLE Laptop (
    Id int(11) NOT NULL,
    Name varchar(250) NOT NULL,
    Price float NOT NULL,
    Purchase_date Date NOT NULL,
    PRIMARY KEY (Id)
  )
"""
```

Agora é só importar essa tabela e utilizar:

[create_table_from_sql.py](src/create_table_from_sql.py)
```python
import mysql.connector

from sql.create_table import Laptop_tb

try:
  connection = mysql.connector.connect(
    host='localhost',
    database='Electronics',
    user='root',
    password='toor'
  )
except mysql.connector.Error as error:
  print("Failed to create table in MySQL: {}".format(error))
else:
  cursor = connection.cursor()
  result = cursor.execute(Laptop_tb)
  print("Laptop Table created successfully!")
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed.")
```

**OUTPUT:**  
```python
Laptop Table created successfully!
MySQL connection is closed.
```

---

**REFERENCES:**  
[Create MySQL table from Python](https://pynative.com/python-mysql-database-connection/#h-create-mysql-table-from-python)  

---

**Rodrigo Leite -** *drigols*
