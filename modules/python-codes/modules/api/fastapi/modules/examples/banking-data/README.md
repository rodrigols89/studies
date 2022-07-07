# ANZ Banking Data

> This example will follow the tutorial [How to Build a REST API Endpoint on Top of an Existing Legacy Database Using FastAPI](https://python.plainenglish.io/how-to-build-a-rest-api-endpoint-on-top-of-an-existing-legacy-database-using-fastapi-489f38feab98).

## Contents

 - [Creating a Database with Docker](#db)
 - [Get data from Kaggle](#kaggle)
 - [Inserting data into the Database](#insert)
 - [Create database connection for FastAPI use](#connection-fastapi)
 - [Creating models](#models)
 - [Creating the schemas](#schemas)
 - [Creating the CRUD](#crud)
 - [Implementing main.py](#main)

---

<div id="db"></div>

## Creating a Database with Docker

The first step will be create a Database:

[docker-compose.yml](docker-compose.yml)
```
version: '3.9'
services:
  db:
    container_name: banking-data
    image: mysql:latest
    restart: always
    environment:
      MYSQL_HOST: localhost
      MYSQL_DATABASE: my-bank
      MYSQL_ROOT_PASSWORD: toor
    ports:
      - "3306:3306"
```

---

<div id="kaggle"></div>

## Get data from Kaggle

Now, let's get source data from Kaggle:

[ANZ Banking Data](https://www.kaggle.com/datasets/prateekmaj21/anz-banking-data)

---

<div id="insert"></div>

## Inserting data into the Database

Now, let's insert data from CSV to Database:

[insert_script.py](insert_script.py)
```python
import mysql.connector
import sqlalchemy
import pandas as pd
import numpy as np

# Database settings.
username: str = "root"
password: str = "toor"
hostname: str = "localhost"
database: str = "my-bank"

# Database Connection (engine)
engine = sqlalchemy.create_engine(
    f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
)

# Get data from CSV (Improve memory usage)
dfi = pd.read_csv(
    "dataset/ANZ.csv",
    dtype={
        'status':'string',
        'card_present_flag':'string',
        'bpay_biller_code':'string',
        'account':'string',
        'currency':'string',
        'long_lat':'string',
        'txn_description':'string',
        'merchant_id':'string',
        'merchant_code':'float16',
        'first_name':'string',
        'balance':'float16',
        'date':'string',
        'gender':'string',
        'age':'int8',
        'merchant_suburb':'string',
        'merchant_state':'string',
        'extraction':'string',
        'amount':'float16',
        'transaction_id':'string',
        'country':'string',
        'customer_id':'string',
        'merchant_long_lat':'string',
        'movement':'string',
    }
)

dfi = dfi.replace([np.inf,-np.inf],np.nan)
df2 = dfi.replace(np.nan, '', regex=True)
df2 = df2.rename(columns={"date":"transaction_date"})
df2 = df2.rename(columns={"extraction":"extraction_timestamp"})
df2 = df2.rename(columns={"amount":"transaction_amount"})
df2['merchant_code'] = df2['merchant_code'].replace("",0.0)

# Insert the data to the database using to_sql method.
df2.to_sql(
    name='financial_data',
    con=engine,
    index=False,
    if_exists='append'
)
```

---

<div id="connection-fastapi"></div>

## Create database connection for FastAPI use

The first thing we need to do is connect to the database. We do this using SQLAlchemy from the file [database.py](database.py):

```python
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
```

---

<div id="models"></div>

## Creating models

Once we have connected to the database the next step is to create **models** in SQLAlchemy.

> A model in the high-level framework language is the equivalent of a table in a database.

 - Therefore we are able to create classes that represent the underlying database tables and the variables corresponding to the columns of that table.
 - Also, any relationship between tables should be declared here.

[models.py](models.py)
```python
from sqlalchemy import Boolean, Column, Integer, String, Date, DateTime, Float, Text
from database import Base


class FinanceData(Base):

    __tablename__ = "financial_data"

    status = Column(Text)
    card_present_flag = Column(Text)
    bpay_biller_code = Column(Text)
    account = Column(Text)
    currency = Column(Text)
    long_lat = Column(Text)
    txn_description = Column(Text)
    merchant_id = Column(Text)
    merchant_code = Column(Float)
    first_name = Column(Text)
    balance = Column(Text)
    transaction_date = Column(Date)
    gender = Column(Text)
    age = Column(Integer)
    merchant_suburb = Column(Text)
    merchant_state = Column(Text)
    extraction_timestamp = Column(DateTime)
    transaction_amount = Column(Float)
    transaction_id = Column(Text,primary_key=True)
    country = Column(Text)
    customer_id = Column(Text)
    merchant_long_lat = Column(Text)
    movement = Column(Text)
```

---

<div id="schemas"></div>

## Creating the schemas

After we have done the mapping , we then need to create a **schema**, once the data has been retrieved by SQLAlchemy using the connection engine it then passes through pydantic (which is a library within fastapi that performs data validation and settings management using python type annotations. pydantic enforces type hints at runtime, and provides user-friendly errors when data is invalid.)

[schemas.py](schemas.py)
```python
from typing import Optional
from pydantic import BaseModel
from datetime import datetime,date

class FinanceData(BaseModel):
    status: str
    card_present_flag: str
    bpay_biller_code: str
    account: str
    currency: str
    long_lat: str
    txn_description: str
    merchant_id: str
    merchant_code: float
    first_name: str
    balance: str
    transaction_date: str
    gender: str
    age: int
    merchant_suburb: str
    merchant_state: str
    extraction_timestamp: datetime
    transaction_amount: float
    transaction_id: str
    country: str
    customer_id: str
    merchant_long_lat: str
    movement: str

    class Config:
        orm_mode = True
```

---

<div id="crud"></div>

## Creating the CRUD

The next step after high-level data validation would be to write functions that do the actual querying of the database using the SQLAlchemy syntax.

[crud.py](crud.py)
```python
from sqlalchemy.orm import Session
import models, schemas

def get_financedata(db: Session, skip: int=0,limit: int=1000):
 return db.query(models.FinanceData).offset(skip).limit(limit).all()
```

In the code above we create a function called get_financedata with the following:

 - **db:Session**
   - Which is passed the current db session which we will create.
 - **skip**
   - which implies skipping **n** number of records and limit can be used to limit the number of returned entries.
 - **db.query(models.FinanceData).offset(skip).limit(limit).all()**
   - This is SQLAlchemy syntax that queries the models from **models.py** we created earlier to give us results from the database.

---

<div id="main"></div>

## Implementing main.py

Finally, we go to our **main.py** file where we will put the final touches to our project/app. Here we will initialize our FastAPI app and create functions that receive HTTP requests in the paths **/finance-data**:

[main.py](main.py)
```python
from database import SessionLocal,engine
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud, models,schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/finance-data", response_model=list[schemas.FinanceData])
def read_financedata(
    skip: int=0,
    limit: int=1000,
    db: Session = Depends(get_db)
):
    finance_data = crud.get_financedata(db,skip=skip,limit=limit)
    return finance_data
```

Now just run [main.py](main.py):

```python
uvicorn main:app --reload
```

---

**REFERENCE:**  
[How to Build a REST API Endpoint on Top of an Existing Legacy Database Using FastAPI](https://python.plainenglish.io/how-to-build-a-rest-api-endpoint-on-top-of-an-existing-legacy-database-using-fastapi-489f38feab98)

---

**Rodrigo Leite -** *drigols*
