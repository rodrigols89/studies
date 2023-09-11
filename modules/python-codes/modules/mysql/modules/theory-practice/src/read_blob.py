import mysql.connector


sql_fetch_blob_query = """
  SELECT * from python_employee where id = %s
"""


def write_file(data, filename):
  # Convert binary data to proper format and write it on Hard Disk
  with open(filename, 'wb') as file:
    file.write(data)


def readBLOB(id, photo, biodata):
  print("Reading BLOB data from python_employee table")
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='python_db',
      user='root',
      password='toor')
  except mysql.connector.Error as error:
    print("Error while connecting to MySQ {}".format(error))
  else:
    cursor = connection.cursor() # cursor instance.

    cursor.execute(sql_fetch_blob_query, (id,))
    record = cursor.fetchall()
    for row in record:
      print("Id = ", row[0], )
      print("Name = ", row[1])
      image = row[2]
      file = row[3]
      print("Storing employee image and bio-data on disk \n")
      write_file(image, photo)
      write_file(file, biodata)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()
      print("MySQL connection is closed")


readBLOB(
  id=1,
  photo="../resources/image_downloaded.jpg",
  biodata="../resources/biodata_downloaded.txt"
)
