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
