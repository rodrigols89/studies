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
