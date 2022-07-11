# Model → Schema

 - A **model** in the high-level framework language is the equivalent of a table in a database:
   - **SQLAlchemy** model.
 - A **schema** is a mapping for a model.
   - **Pydantic** model (Pydantic allows us to validate a schema data).

## Contents

 - [Mapping "financial_data" table](#financial-data)

---

<div id="financial-data"></div>

## Mapping "financial_data" table

To mapping **"financial_data"** table first, let's create a model:

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

Now, let's create the **schema**:

```python
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

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

**NOTE:**  
We are using Pydantic to validate the data types.

---

**REFERENCES:**  
[]()  

---

**Rodrigo Leite -** *drigols*
