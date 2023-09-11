# SUS (Brazil health system) Information System

## Contents

 - [01 - Introduction to the System](#intro)
 - [02 - Creating SUS Database](#create-database)
 - [03 - Connecting to the SUS Database](#connecting)
 - [04 - Creating tables Hospital and Doctor](#create-table)
 - [05 - Inserting data in the tables](#inserting-data)
 - [06 - Fetch Hospital and Doctor Information using "hospital Id" and "doctor Id"](#fetch-by-id)
 - [07 - Closing Database Connection](#closing)

---

<div id="intro"></div>

## 01 - Introduction to the System

In this exercise, we go implementing the **SUS (Brazil health system) Information System**. Initially, we have two tables:

 - Hospital
 - Doctor

![model](resources/model.png)  

---

<div id="create-database"></div>

## 02 - Creating SUS Database

First, we need create a Database **SUS (Brazil health system)** on our *MySQL Server*:

```python
mysql> CREATE DATABASE SUS;
```

```python
mysql> SHOW DATABASES;
```

**OUTPUT:**  
```python
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
| sus                |
+--------------------+
3 rows in set (0.00 sec)
```

Great, now we have the **SUS** Database to work with.

---

<div id="connecting"></div>

## 03 - Connecting to the SUS Database

Now, we have **SUS** Database, we go create connection. For our, example we create the MySQL class and constructor for represent the connection.

See example below:

[database.py](hospital/database.py)
```python
import mysql.connector

from mysql.connector import Error


class MySQL:


  def __init__(self, host='localhost', database=None, user=None, password=None):
    if database == None:
      return print("Please, enter your Database name!")
    elif user == None:
      return print("Please, enter your user name!")
    elif password == None:
      return print("Please, enter your password!")
    else:
      try:
        connection = mysql.connector.connect(
          host=host,
          database=database,
          user=user,
          password=password
        )
        if connection.is_connected():
          db_Info = connection.get_server_info()
          print("Connected to MySQL Server version ", db_Info)
          cursor = connection.cursor()
          cursor.execute("select database();")
          record = cursor.fetchone()
          print("You're connected to database:", record)
      except Error as e:
        print("Error while connecting to MySQL", e)
```

For test we create [main.py](main.py) file:

[main.py](main.py)
```python
from hospital.database import MySQL

if __name__ =="__main__":

  my_db = MySQL(
    database="SUS",
    user="root",
    password="toor"
  )
```

**OUTPUT:**  
```python
Connected to MySQL Server version  5.7.38-log
You're connected to database: ('sus',)
```

**NOTE:**  
Great, we are connected!

---

<div id="create-table"></div>

## 04 - Creating tables Hospital and Doctor

Now, we go implement a method to create tables from ready SQL scripts:

[database.py](hospital/database.py)
```python
def create_table(self, sql_script=None):

  if sql_script == None:
    return print("Please, enter your SQL Script to Create Table.")
  else:
    try:
      cursor = self.connection.cursor()
      result = cursor.execute(sql_script)
      print("Table created successfully!")
    except mysql.connector.Error as error:
      print("Failed to create table in MySQL: {}".format(error))
    finally:
      cursor.close()
```

[main.py](main.py)
```python
from hospital.database import MySQL

from sql.create_table import Hospital, Doctor


if __name__ =="__main__":

  my_db = MySQL(
    database="SUS",
    user="root",
    password="toor"
  )

  # Create table Hospital and Doctor from ready SQL scripts.
  my_db.create_table(Hospital)
  my_db.create_table(Doctor)
```

**OUTPUT:**  
```python
Connected to MySQL Server version  5.7.38-log
You're connected to database: ('sus',)
Table created successfully!
Table created successfully!
```

**NOTE:**  
You can test in your Database:

```python
show tables;
```

**OUTPUT**  
```python
+---------------+
| Tables_in_sus |
+---------------+
| doctor        |
| hospital      |
+---------------+
```

---

<div id="inserting-data"></div>

## 05 - Inserting data in the tables

Now, we go insert data in the tables **Hospital** and **Doctor** from ready SQL scripts:

[database.py](hospital/database.py)
```python
def insert_data(self, insert_query=None, records_to_insert=None):

  if insert_query == None:
    return print("Please, enter your SQL Script to insert data in the table.")
  elif records_to_insert == None:
    return print("Please, enter your records data to insert data in the table.")
  else:
    try:
      cursor = self.connection.cursor()
      cursor.executemany(insert_query, records_to_insert)
      self.connection.commit()
      print(cursor.rowcount, "Record inserted successfully into table")
    except mysql.connector.Error as error:
      print("Failed to insert records into MySQL table: {}".format(error))
    finally:
      cursor.close()
```

[main.py](main.py)
```python
from hospital.database import MySQL

from sql.create_table import Hospital, Doctor
from sql.insert_into_scripts import insert_into_hospital_table, insert_into_doctor_table


if __name__ =="__main__":

  hospital_records = [
    ('1', 'Mayo Clinic', 200), 
    ('2', 'Cleveland Clinic', 400), 
    ('3', 'Johns Hopkins', 1000), 
    ('4', 'UCLA Medical Center', 1500)
  ]

  doctor_records = [
    ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', None), 
    ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', None), 
    ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', None), 
    ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', None), 
    ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', None), 
    ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', None), 
    ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', None), 
    ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', None)
  ]

  my_db = MySQL(
    database="SUS",
    user="root",
    password="toor"
  )

  # Create table Hospital and Doctor from ready SQL scripts.
  #my_db.create_table(Hospital)
  #my_db.create_table(Doctor)

  # Insert data into hospital table.
  my_db.insert_data(
    insert_query=insert_into_hospital_table,
    records_to_insert=hospital_records
  )
  # Insert data into doctor table.
  my_db.insert_data(
    insert_query=insert_into_doctor_table,
    records_to_insert=doctor_records
  )
```

**OUTPUT:**  
```python
Connected to MySQL Server version  5.7.38-log
You're connected to database: ('sus',)
4 Record inserted successfully into table
8 Record inserted successfully into table
```

**NOTE:**  
You can test in your Database:

```python
mysql> select * from hospital; select * from doctor;
```

**OUTPUT**  
```python
+-------------+---------------------+-----------+
| Hospital_Id | Hospital_Name       | Bed_Count |
+-------------+---------------------+-----------+
|           1 | Mayo Clinic         |       200 |
|           2 | Cleveland Clinic    |       400 |
|           3 | Johns Hopkins       |      1000 |
|           4 | UCLA Medical Center |      1500 |
+-------------+---------------------+-----------+
4 rows in set (0.00 sec)

+-----------+-------------+-------------+--------------+---------------+--------+------------+
| Doctor_Id | Doctor_Name | Hospital_Id | Joining_Date | Speciality    | Salary | Experience |
+-----------+-------------+-------------+--------------+---------------+--------+------------+
|       101 | David       |           1 | 2005-02-10   | Pediatric     |  40000 |       NULL |
|       102 | Michael     |           1 | 2018-07-23   | Oncologist    |  20000 |       NULL |
|       103 | Susan       |           2 | 2016-05-19   | Garnacologist |  25000 |       NULL |
|       104 | Robert      |           2 | 2017-12-28   | Pediatric     |  28000 |       NULL |
|       105 | Linda       |           3 | 2004-06-04   | Garnacologist |  42000 |       NULL |
|       106 | William     |           3 | 2012-09-11   | Dermatologist |  30000 |       NULL |
|       107 | Richard     |           4 | 2014-08-21   | Garnacologist |  32000 |       NULL |
|       108 | Karen       |           4 | 2011-10-17   | Radiologist   |  30000 |       NULL |
+-----------+-------------+-------------+--------------+---------------+--------+------------+
8 rows in set (0.00 sec)
```

---

<div id="fetch-by-id"></div>

## 06 - Fetch Hospital and Doctor Information using "hospital Id" and "doctor Id"

Now we go Implement the functionality to read the details of a given doctor from the doctor table and Hospital from the hospital table. I.e., read records from Hospital and Doctor Table as per given hospital Id and Doctor Id. 

See code below to understand how it's working:

[database.py](hospital/database.py)
```python
def get_hospital_detail(self, hospital_id=None):
  if hospital_id == None:
    return print("Please, enter Hospital ID.")
  else:
    try:
      cursor = self.connection.cursor()
      select_query = """select * from Hospital where Hospital_Id = %s"""
      cursor.execute(select_query, (hospital_id,))
      records = cursor.fetchall()
      print("Printing Hospital record")
      for row in records:
          print("Hospital Id:", row[0], )
          print("Hospital Name:", row[1])
          print("Bed Count:", row[2])
    except (Exception, mysql.connector.Error) as error:
      print("Error while getting data", error)
    finally:
      cursor.close()


def get_doctor_detail(self, doctor_id=None):
  if doctor_id == None:
    return print("Please, enter Doctor ID.")
  else:
    try:
      cursor = self.connection.cursor()
      select_query = """select * from Doctor where Doctor_Id = %s"""
      cursor.execute(select_query, (doctor_id,))
      records = cursor.fetchall()
      print("Printing Doctor record")
      for row in records:
        print("Doctor Id:", row[0])
        print("Doctor Name:", row[1])
        print("Hospital Id:", row[2])
        print("Joining Date:", row[3])
        print("Specialty:", row[4])
        print("Salary:", row[5])
        print("Experience:", row[6])
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
    finally:
      cursor.close()
```

[main.py](main.py)
```python
# Get hospital and Doctor details by ID.
my_db.get_hospital_detail(2)
print("\n")
my_db.get_doctor_detail(105)
```

**OUTPUT:**
```python
Printing Hospital record
Hospital Id: 2
Hospital Name: Cleveland Clinic
Bed Count: 400


Printing Doctor record
Doctor Id: 105
Doctor Name: Linda
Hospital Id: 3
Joining Date: 2004-06-04
Specialty: Garnacologist
Salary: 42000
Experience: None
```

---

<div id="closing"></div>

## 07 - Closing Database Connection

Just to finalizer we need closing the Database connection:


[database.py](hospital/database.py)
```python
def close_connection(self):
  if self.connection.is_connected():
    self.connection.close()
    print("MySQL connection is closed.")
```

[main.py](main.py)
```python
# Closing Databaseconnection.
my_db.close_connection()
```

**OUTPUT:**  
```python
MySQL connection is closed.
```

---

**REFERENCES:**  
[Python Database Programming Exercise](https://pynative.com/python-database-programming-exercise-with-solution/)  

---

**Rodrigo Leite -** *drigols*
