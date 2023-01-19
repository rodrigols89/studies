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
