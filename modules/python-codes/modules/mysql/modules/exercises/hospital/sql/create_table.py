Hospital = """
CREATE TABLE Hospital (
  Hospital_Id INT UNSIGNED NOT NULL, 
  Hospital_Name TEXT NOT NULL, 
  Bed_Count INT, 
  PRIMARY KEY (Hospital_Id)
);
"""


Doctor = """
CREATE TABLE Doctor(
  Doctor_Id INT UNSIGNED NOT NULL,
  Doctor_Name TEXT NOT NULL, 
  Hospital_Id INT NOT NULL, 
  Joining_Date DATE NOT NULL, 
  Speciality TEXT NULL, 
  Salary INT NULL, 
  Experience INT NULL, 
  PRIMARY KEY (Doctor_Id)
);
"""
