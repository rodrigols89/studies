from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from driver_models import StudentModel


# Database settings
username = "root"
password = "toor"
database = "mysql-db"
host="localhost"
port="3310"
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

try:
    with Session(engine) as session:
        try:
            # Example 1: Select all students
            students = session.query(StudentModel).all()
            print("============================= ( SELECT ALL ) =============================")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")

            # Example 2: Select students based on specific criteria
            students = session.query(StudentModel).filter_by(name='Rodrigo', lastname='Leite').all()
            print("===== ( SELECT WHERE (.filter_by) name='Rodrigo' AND lastname='Doe' ) =====")
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")

            # Example 3: Select only one student based on ID
            student = session.query(StudentModel).filter(StudentModel.id == 10).first()
            print("===== ( SELECT WHERE (.filter_by) (StudentModel.id == 1).first() ) ========")
            if student:
                print(f"ID: {student.id}, Name: {student.name}, Lastname: {student.lastname}")
            else:
                print("Student not found.")
        except Exception as e:
            print("An error occurred during the SELECT (session.query) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
