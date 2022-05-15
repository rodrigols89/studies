# Inserindos dados em tabelas (Insert into)

## Contents

 - [01 - Inserindo dados em uma tabela em um Banco de Dados MySQL em Python](#insert-intro)
 - [02 - Inserindo dados de uma variável ou passadas pelo usuário em uma Tabela](#variables)
 - [03 - Inserindo várias linhas (registro) na tabela MySQL usando o método executemany() do objeto cursor()](#executemany)
 - [04 - Inserir timestamp e DateTime em uma tabela MySQL usando Python](#dateTime)

---

<div id="insert-intro"></div>

## 01 - Inserindo dados em uma tabela em um Banco de Dados MySQL em Python

Para inserir dados em uma tabela de um Banco de Dados MySQL em Python é muito simples. Por exemplo, vejam o código abaixo:

[insert_into.py](src/insert_into.py)
```python
import mysql.connector

insert_query = """
  INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
  VALUES 
                     (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14')
"""

try:
  connection = mysql.connector.connect(
    host='localhost',
    database='electronics',
    user='root',
    password='toor'
  )
except mysql.connector.Error as error:
  print("Failed to insert record into Laptop table {}".format(error))
else:
  cursor = connection.cursor()
  cursor.execute(insert_query)
  connection.commit()
  print(cursor.rowcount, "Record inserted successfully into Laptop table")
  cursor.close()
finally:
  if connection.is_connected():
    connection.close()
    print("MySQL connection is closed")
```

**OUTPUT:**  
```python
1 Record inserted successfully into Laptop table
MySQL connection is closed
```

**NOTE:**  
Ótimo, conseguimos inserir um registro na nossa tabela **"laptop"**, agora é só utilizar a consulta `"select * from laptop"` e ver o registro no Banco de Dados:

```python
select * from laptop
```

**OUTPUT:**  
```python
+----+---------------------+-------+---------------+
| Id | Name                | Price | Purchase_date |
+----+---------------------+-------+---------------+
| 15 | Lenovo ThinkPad P71 |  6459 | 2019-08-14    |
+----+---------------------+-------+---------------+
```

---

<div id="variables"></div>

## 02 - Inserindo dados de uma variável ou passadas pelo usuário em uma Tabela

 - Às vezes você precisa inserir um valor de uma variável Python na coluna de uma tabela. Por exemplo, no formulário de inscrição do usuário, o usuário insere seus detalhes.
 - Você também pode pegar esses valores em variáveis ​​Python e inseri-los em uma tabela.

**NOTE:**  
Uma das maneiras de trabalhar com esses valores que serão inseridos (passados) é utilizando **(%s)** no lugar de onde as variáveis serão inseridas e passá-las como argumento (por exemplo, uma função).

Vejam o exemplo abaixo para ficar mais claro:

[insert_into_function.py](src/insert_into_function.py)
```python
import mysql.connector

def insert_varibles_into_table(id, name, price, purchase_date):
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='Electronics',
      user='root',
      password='toor'
    )
  except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))
  else:
      insert_query = """
        INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
        VALUES (%s, %s, %s, %s)
      """
      cursor = connection.cursor()
      record = (id, name, price, purchase_date)
      cursor.execute(insert_query, record)
      connection.commit()
      print("Record inserted successfully into Laptop table")
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()
      print("MySQL connection is closed")

# Drive
insert_varibles_into_table(1, 'Acer', 6999, '2019-04-14')
insert_varibles_into_table(2, 'MacBook Pro', 2499, '2019-06-20')
```

**OUTPUT:**  
```python
+----+---------------------+-------+---------------+
| Id | Name                | Price | Purchase_date |
+----+---------------------+-------+---------------+
|  1 | Acer                |  6999 | 2019-04-14    |
|  2 | MacBook Pro         |  2499 | 2019-06-20    |
| 15 | Lenovo ThinkPad P71 |  6459 | 2019-08-14    |
+----+---------------------+-------+---------------+
```

**NOTES:**  
As observações mais importantes dos códigos acima são as seguintes:

 - **O méotodo cursor.execute() agora recebe dois argumentos:**
   - Um modelo da query que nós queremos executar.
   - E o nome das colunas/campos/atributos que receberão os dados.

---

<div id="executemany"></div>

## 03 - Inserindo várias linhas (registros) na tabela MySQL usando o método executemany() do objeto cursor()

No exemplo anterior, usamos o método **execute()** do objeto **cursor()** para inserir `um único registro`. Mas, e se você quiser inserir várias linhas (registros) em uma tabela em uma única consulta de inserção do aplicativo Python?

> Para isso nós podemos utilizar o método **executemany()** do objeto **cursor()** para inserir vários registros em uma tabela.

Vejam o exemplo abaixo:

[insert_into_executemany.py](src/insert_into_executemany.py)
```python
import mysql.connector

insert_query = """
  INSERT INTO Laptop (Id, Name, Price, Purchase_date)
                      VALUES (%s, %s, %s, %s)
"""

records_to_insert = [
  (4, 'HP Pavilion Power', 1999, '2019-01-11'),
  (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
  (6, 'Microsoft Surface', 2330, '2019-07-23')
]

try:
  connection = mysql.connector.connect(
    host='localhost',
    database='Electronics',
    user='root',
    password='toor'
  )
except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))
else:
  cursor = connection.cursor()
  cursor.executemany(insert_query, records_to_insert)
  connection.commit()
  print(cursor.rowcount, "Record inserted successfully into Laptop table")
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
```

**OUTPUT:**  
```python
3 Record inserted successfully into Laptop table
MySQL connection is closed
```

Agora é só visualizar o resultado no nosso Banco de Dados:

```python
select * from laptop
```

**OUTPUT:**  
```python
+----+---------------------+-------+---------------+
| Id | Name                | Price | Purchase_date |
+----+---------------------+-------+---------------+
|  1 | Acer                |  6999 | 2019-04-14    |
|  2 | MacBook Pro         |  2499 | 2019-06-20    |
|  4 | HP Pavilion Power   |  1999 | 2019-01-11    |
|  5 | MSI WS75 9TL-496    |  5799 | 2019-02-27    |
|  6 | Microsoft Surface   |  2330 | 2019-07-23    |
| 15 | Lenovo ThinkPad P71 |  6459 | 2019-08-14    |
+----+---------------------+-------+---------------+
```

**NOTE:**  
Uma observação final aqui é que nós estamos utilzando **cursor.rowcount** que retorna o número de registros inseridos.

---

<div id="dateTime"></div>

## 04 - Inserir timestamp e DateTime em uma tabela MySQL usando Python

Por exemplo, você tem uma coluna de data em uma tabela MySQL. Vamos ver como preparar uma consulta de inserção para adicionar DateTime em uma tabela do Python:

[timestamp.py](src/timestamp.py)
```python
from datetime import datetime

import mysql.connector

# Query
insert_query = """
  INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                      VALUES (%s, %s, %s, %s)
"""

# Prepare date (timestamp).
current_date = datetime.now()
# convert date in the format you want
formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')

# Value passed to MySQL table.
insert_tuple = (3, 'Acer Predator Triton', 2435, current_date)

try:
  connection = mysql.connector.connect(
    host='localhost',
    database='Electronics',
    user='root',
    password='toor'
  )
except mysql.connector.Error as error:
  print("Failed to insert into MySQL table {}".format(error))
else:
  cursor = connection.cursor()
  result = cursor.execute(insert_query, insert_tuple)
  connection.commit()
  print("Date Record inserted successfully!")
finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed.")
```

**OUTPUT:**  
```python
Date Record inserted successfully!
MySQL connection is closed.
```

Novamente, vamos verificar se o nosso registro foi adicionado:

```python
select * from laptop
```

**OUTPUT:**  
```python
+----+----------------------+-------+---------------+
| Id | Name                 | Price | Purchase_date |
+----+----------------------+-------+---------------+
|  1 | Acer                 |  6999 | 2019-04-14    |
|  2 | MacBook Pro          |  2499 | 2019-06-20    |
|  3 | Acer Predator Triton |  2435 | 2022-05-15    |
|  4 | HP Pavilion Power    |  1999 | 2019-01-11    |
|  5 | MSI WS75 9TL-496     |  5799 | 2019-02-27    |
|  6 | Microsoft Surface    |  2330 | 2019-07-23    |
| 15 | Lenovo ThinkPad P71  |  6459 | 2019-08-14    |
+----+----------------------+-------+---------------+
```

---

**REFERENCES:**  
[Python Insert Into MySQL Table](https://pynative.com/python-mysql-insert-data-into-database-table/)  

---

**Rodrigo Leite -** *drigols*
