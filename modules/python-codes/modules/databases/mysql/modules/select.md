# Selecionando linhas (registros) de uma tabela MySQL em Python

## Contents

 - [01 - Preparando a tabela](#preparing-table)
 - [02 - Exibindo linhas (registros) de uma tabela em Python](#example-01)

---

<div id="preparing-table"></div>

## 01 - Preparando a tabela

Antes de nós iniciarmos nossos estudos sobre **SELECT** para fazer consultas SQL vamos criar e adicionar registros em nossa tabela. Para isso, vejam o exemplo abaixo:

```python
create database Electronics;
```

```python
CREATE TABLE `laptop` (
  `Id` int(11) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Price` float NOT NULL,
  `Purchase_date` date NOT NULL
);
```

```python
ALTER TABLE `laptop`
  ADD PRIMARY KEY (`Id`);
COMMIT;
```

```python
INSERT INTO `laptop` (`Id`, `Name`, `Price`, `Purchase_date`) VALUES
(1, 'Lenovo ThinkPad P71', 6459, '2019-08-14'),
(2, 'Area 51M', 6999, '2019-04-14'),
(3, 'MacBook Pro', 2499, '2019-06-20'),
(4, 'HP Pavilion Power', 1999, '2019-01-11'),
(5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
(6, 'Microsoft Surface', 2330, '2019-07-23'),
(7, 'Acer Predator Triton', 2435, '2019-08-15');
```

```python
select * from laptop;
```

**OUTPUT:**  
```python
+----+----------------------+-------+---------------+
| Id | Name                 | Price | Purchase_date |
+----+----------------------+-------+---------------+
|  1 | Lenovo ThinkPad P71  |  6459 | 2019-08-14    |
|  2 | Area 51M             |  6999 | 2019-04-14    |
|  3 | MacBook Pro          |  2499 | 2019-06-20    |
|  4 | HP Pavilion Power    |  1999 | 2019-01-11    |
|  5 | MSI WS75 9TL-496     |  5799 | 2019-02-27    |
|  6 | Microsoft Surface    |  2330 | 2019-07-23    |
|  7 | Acer Predator Triton |  2435 | 2019-08-15    |
+----+----------------------+-------+---------------+
```

**NOTE:**  
Ótimo preparamos a tabela em que vamos trabalhar inclusive mostramos como exibir todos os registros em linha de comando. Agora vem a pergunta-chave:

> **Como mostra isso em Python?**

---

<div id="example-01"></div>

## 02 - Exibindo linhas (registros) de uma tabela em Python

Para o exemplo abaixo, estamos buscando todas as linhas da tabela **Laptop** e copiando-as em variáveis ​​Python para que possamos usá-las em nosso programa:

[select-v1.py](src/select-v1.py)
```python
import mysql.connector

sql_select_Query = "select * from Laptop"

try:
  connection = mysql.connector.connect(
    host='localhost',
    database='electronics',
    user='root',
    password='toor'
  )
except mysql.connector.Error as e:
  print("Error while connecting to MySQL", e)
else:
  try:
    cursor = connection.cursor() # Cursor instance.
    cursor.execute(sql_select_Query) # Run SQL Query.
    records = cursor.fetchall() # Get all records.

    # Print data in the console.
    print("Total number of rows in table: ", cursor.rowcount)
    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
  except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
  if connection.is_connected():
    connection.close()
    cursor.close()
    print("MySQL connection is closed")
```

**OUTPUT:**  
````python
Total number of rows in table:  7

Printing each row
Id =  1
Name =  Lenovo ThinkPad P71
Price  =  6459.0
Purchase date  =  2019-08-14

Id =  2
Name =  Area 51M
Price  =  6999.0
Purchase date  =  2019-04-14

Id =  3
Name =  MacBook Pro
Price  =  2499.0
Purchase date  =  2019-06-20

Id =  4
Name =  HP Pavilion Power
Price  =  1999.0
Purchase date  =  2019-01-11

Id =  5
Name =  MSI WS75 9TL-496
Price  =  5799.0
Purchase date  =  2019-02-27

Id =  6
Name =  Microsoft Surface
Price  =  2330.0
Purchase date  =  2019-07-23

Id =  7
Name =  Acer Predator Triton
Price  =  2435.0
Purchase date  =  2019-08-15

MySQL connection is closed
````

**NOTE:**  
Vejam que lindo, mas temos uma observação aqui, nós estamos utilizando o método **cursor.fetchall()**. Esse método serve para pegar os dados que foram retornados do método **cursor.execute()**.

> Existem os seguintes métodos para buscar dados retornados por um **cursor.execute()**

 - **cursor.fetchall()**
   - Para buscar todas as linhas.
 - **cursor.fetchone()**
   - Para buscar uma única linha.
 - **cursor.fetchmany(SIZE)**
   - Para buscar linhas limitadas.

---

**REFERENCES:**  
[Python Select from MySQL Table](https://pynative.com/python-mysql-select-query-to-fetch-data/)  

---

**Rodrigo Leite -** *drigols*
