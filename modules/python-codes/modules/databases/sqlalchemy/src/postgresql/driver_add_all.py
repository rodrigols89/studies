from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from driver_models import StudentModel


# Database settings
username = "postgres"
password = "toor"
database = "postgre_db"
host="localhost"
port="5432"
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}",
    echo=False,
)

data = [
    {"name": "John", "lastname": "Doe"},
    {"name": "Jane", "lastname": "Smith"},
    {"name": "Rodrigo", "lastname": "Leite"},
    {"name": "Ricardo", "lastname": "Bruno"},
    {"name": "Mary", "lastname": "Jane"},
    {"name": "Richard", "lastname": "Belmont"},
    {"name": "Isaac", "lastname": "Newton"},
    {"name": "Lionel", "lastname": "Messi"},
    {"name": "Cristiano", "lastname": "Ronaldo"},
    {"name": "Jesus", "lastname": "Cristo"},
]
students = [StudentModel(name=item["name"], lastname=item["lastname"]) for item in data]

try:
    with Session(engine) as session:
        try:
            session.add_all(students)
            session.commit()
            print("Insert (add_all) operation completed successfully!")
        except Exception as e:
            session.rollback()
            print("An error occurred during the insert (add_all) operation:", str(e))
except Exception as e:
    print("An error occurred while initializing the session:", str(e))
