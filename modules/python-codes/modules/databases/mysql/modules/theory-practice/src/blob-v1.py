import mysql.connector


insert_blob_query = """
  INSERT INTO python_employee (id, name, photo, biodata)
                       VALUES (%s,%s,%s,%s)
"""


def convertToBinaryData(filename):
  # Convert digital data to binary format
  with open(filename, 'rb') as file:
    binaryData = file.read()
  return binaryData


def insertBLOB(id, name, photo, biodata):
  print("Inserting BLOB into python_employee table")
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='python_db',
      user='root',
      password='toor'
    )
  except mysql.connector.Error as error:
      print("Failed inserting BLOB data into MySQL table {}".format(error))
  else:
    cursor = connection.cursor() # Cursor instance.

    # Convert data to BLOB.
    photo_converted = convertToBinaryData(photo)
    biodata_converted = convertToBinaryData(biodata)
    # Convert data into tuple format
    insert_blob_tuple = (id, name, photo_converted, biodata_converted)
    print(insert_blob_tuple)

    #result = cursor.execute(insert_blob_query, insert_blob_tuple)
    #connection.commit()
    #print("Image and file inserted successfully as a BLOB into python_employee table", result)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()
      print("MySQL connection is closed")


insertBLOB(
  id=3,
  name="Rodrigo",
  photo="../images/profile-picture.jpg",
  biodata="../resources/rodrigo_biodata.txt"
)
