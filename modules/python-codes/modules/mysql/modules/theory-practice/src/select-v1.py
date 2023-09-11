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
