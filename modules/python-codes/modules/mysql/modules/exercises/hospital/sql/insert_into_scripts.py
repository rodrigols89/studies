insert_into_hospital_table = """
INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
VALUES 
(%s, %s, %s);
"""

insert_into_doctor_table = """
INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
VALUES 
(%s, %s, %s, %s, %s, %s, %s);
"""
