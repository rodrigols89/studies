from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database settings.
username: str = "root"
password: str = "toor"
hostname: str = "localhost"
database: str = "my-bank"

# Database Connection (engine)
engine = create_engine(
    f'mysql+pymysql://{username}:{password}@{hostname}/{database}',
    echo=True
)

# Each instance of SessionLocal class will be database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We use declarative_base to return a class which we will inherit from to
# create database models or classes
Base = declarative_base()
