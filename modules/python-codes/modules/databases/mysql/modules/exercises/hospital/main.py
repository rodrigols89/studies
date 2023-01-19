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
  my_db.create_table(Hospital)
  my_db.create_table(Doctor)

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

  # Get hospital and Doctor details by ID.
  my_db.get_hospital_detail(2)
  print("\n")
  my_db.get_doctor_detail(105)

  # Closing Databaseconnection.
  my_db.close_connection()
