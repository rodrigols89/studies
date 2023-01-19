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
