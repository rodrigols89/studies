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
        self.connection = mysql.connector.connect(
          host=host,
          database=database,
          user=user,
          password=password
        )
        if self.connection.is_connected():
          db_Info = self.connection.get_server_info()
          print("Connected to MySQL Server version ", db_Info)
          cursor = self.connection.cursor()
          cursor.execute("select database();")
          record = cursor.fetchone()
          print("You're connected to database:", record)
      except Error as e:
        print("Error while connecting to MySQL:", e)


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


  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("MySQL connection is closed.")
