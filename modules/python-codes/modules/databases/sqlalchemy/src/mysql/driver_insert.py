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

# Create an object (instance) student.
student = StudentModel(name='John', lastname='Doe')

try:
    with Session(engine) as session:
        try:
            session.add(student)
            session.commit()
            print("Insert (add) operation completed successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred during the insert (add) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
