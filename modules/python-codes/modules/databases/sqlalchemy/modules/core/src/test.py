from sqlalchemy import text

from connections import get_engine_connection
from core_model import student as student_tb

engine = get_engine_connection('root', 'toor', 'sqlalchemy-db')

with engine.begin() as connection:
    connection.execute(student_tb.insert(), {"name": "Reginaldo", "Freire": "Gomes"})
