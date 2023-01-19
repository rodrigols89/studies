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
