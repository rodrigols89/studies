from Settings import mysql_settings, postgresql_settings
from SQLAlchemy_Models import Base, HeroModel, StudentModel
from Engine import get_engine


mysql_engine = get_engine(**mysql_settings)
postgresql_engine = get_engine(**postgresql_settings)

from sqlalchemy.orm import declarative_base

Base.metadata.create_all(mysql_engine)
