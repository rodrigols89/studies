# Project Structure | Models | Endpoints | Routes

## Contents

 - [Create a docker compose](#docker-compose)
 - [Create "product" table](#product-table)
 - [Create Files and Folders](#files-folders)
 - [Create Models](#create-models)
 - [Create Database connection and session](#connect-db)
 - [Create API Endpoints](#endpoints)
 - [Create Routes](#routes)

---

<div id="docker-compose"></div>

## Create a docker compose

For this example, the first thing we'll need is create a docker compose:

[docker-compose.yml](docker-compose.yml)
```python
version: '3.9'
services:
  db:
    container_name: mysql
    image: mysql:latest
    environment:
      MYSQL_HOST: localhost
      MYSQL_DATABASE: my_test_db
      MYSQL_ROOT_PASSWORD: toor
    ports:
      - "3306:3306"
```

Now just run:

**CONSOLE:**
```python
sudo docker compose up -d
```

---

<div id="product-table"></dv>

## Create "product" table

Now, let's create a product table:

**CONSOLE:**
```python
sudo docker exec -it mysql bash
```

**CONSOLE:**
```python
mysql --user=root --password=toor my_test_db
```

Finally, let's create a table:

```sql
CREATE TABLE IF NOT EXISTS product(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(1024),
    price BIGINT DEFAULT 0,
    is_available BOOLEAN DEFAULT FALSE,
    seller_email VARCHAR(512),
    deleted BOOLEAN DEFAULT FALSE,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT NULL,
    updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE = INNODB;
```

```sql
SHOW TABLES;

+----------------------+
| Tables_in_my_test_db |
+----------------------+
| product              |
+----------------------+
1 row in set (0.00 sec)
```

---

<div id="files-folders"></div>

## Create Files and Folders

Now, let's create folders and files as shown below to make your project's file structure look like this:

```python
├── sample_fastapi_mysql_app
│   │── env
│   │── db
│   │    └── database.py
│   │
│   ├── endpoints
│   │     └── product.py
│   │     └── user.py
│   │
│   ├── models
│   │     └── models.py
│   │     └── request.py
│   │     └── response.py
│   │
│   ├── routes
│   │     └── api.py
│   │
│   ├── __init__.py
│   ├── main.py
```

---

<div id="create-models"></div>

## Create Models

Now, let's create models

[models/models.py](models/models.py)
```python
from sqlalchemy import Column, INTEGER, String, TIMESTAMP, BIGINT, BOOLEAN, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Base):
    __tablename__ = "product"
    id = Column(INTEGER, primary_key=True)
    name = Column(String(1024), nullable=False)
    price = Column(BIGINT)
    is_available = (Column(BOOLEAN, default=True))
    seller_email = (Column(String(512), nullable=True))
    deleted = (Column(BOOLEAN, default=False))
    created_by = Column(INTEGER, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(INTEGER, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = "user"
    id = Column(INTEGER, primary_key=True)
    first_name = Column(String(512), nullable=False)
    last_name = Column(String(512), nullable=False)
    deleted = (Column(BOOLEAN, default=False))
    created_by = Column(INTEGER, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(INTEGER, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
```

[models/request.py](models/request.py)
```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ProductRequest(BaseModel):
    name: str = Field(None, title="Product Name", max_length=1000)
    price: float = Field(..., gt=0, description="Price of the product")
    is_available: bool = Field(False, description="Value must be either True or False")
    seller_email: EmailStr = Field(None, title="Seller Email")
    created_by: int = Field(None, title="User Id")


class ProductUpdateRequest(BaseModel):
    product_id: int
    name: str = Field(None, title="Product Name", max_length=1000)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    is_available: bool = Field(False, description="Value must be either True or False")
    seller_email: Optional[EmailStr] = Field(None, title="Updater Email")
    updated_by: int = Field(None, title="Updater Id")
```

[models/response.py](models/response.py)
```python
def Response(data, code, message, error):
    return {
        "data": data,
        "code": code,
        "message": message,
        "error": error
    }
```

---

<div id="connect-db"></div>

## Create Database connection and session

Now, let's create Database connection and session:

[db/database.py](db/database.py)
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database settings.
username: str = "root"
password: str = "toor"
hostname: str = "localhost"
servicePort = str = "3306"
database: str = "my_test_db"

MYSQL_URL = f'mysql+pymysql://{username}:{password}@{hostname}:{servicePort}/{database}?charset=utf8'
POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60

class Database():

    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def get_db_connection(self):
        if self.connection_is_active == False:
            connect_args = {"connect_timeout":CONNECT_TIMEOUT}
            try:
                self.engine = create_engine(
                    MYSQL_URL,
                    pool_size=POOL_SIZE,
                    pool_recycle=POOL_RECYCLE,
                    pool_timeout=POOL_TIMEOUT,
                    max_overflow=MAX_OVERFLOW,
                    connect_args=connect_args
                )
                return self.engine
            except Exception as ex:
                print("Error connecting to DB : ", ex)
        return self.engine


    def get_db_session(self, engine):
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            return session
        except Exception as ex:
            print("Error getting DB session : ", ex)
            return None
```

---

<div id="endpoints"></div>

## Create API Endpoints

Now, let's create our API Endpoints:

[endpoints/product.py](endpoints/product.py)
```python
from fastapi import APIRouter

from models.request import ProductRequest, ProductUpdateRequest
from models.response import Response
from models.models import Product

from db.database import Database

from sqlalchemy import and_, desc


# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()


@router.post("/add", response_description="Product data added into the database")
async def add_product(product_req: ProductRequest):
    new_product = Product()
    new_product.name = product_req.name
    new_product.price = product_req.price
    new_product.seller_email = product_req.seller_email
    new_product.is_available = product_req.is_available
    new_product.created_by = product_req.created_by
    new_product_id = None
    session = database.get_db_session(engine)
    session.add(new_product)
    session.flush()
    # get id of the inserted product
    session.refresh(new_product, attribute_names=['id'])
    data = {"product_id": new_product.id}
    session.commit()
    session.close()
    return Response(data, 200, "Product added successfully.", False)


@router.put("/update")
async def update_product(product_update_req: ProductUpdateRequest):
    product_id = product_update_req.product_id
    session = database.get_db_session(engine)
    try:
        is_product_updated = session.query(Product).filter(Product.id == product_id).update({
            Product.name: product_update_req.name, Product.price: product_update_req.price,
            Product.seller_email: product_update_req.seller_email,
            Product.is_available: product_update_req.is_available,
            Product.updated_by: product_update_req.updated_by
        }, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Product updated successfully"
        response_code = 200
        error = False
        if is_product_updated == 1:
            # After successful update, retrieve updated data from db
            data = session.query(Product).filter(
                Product.id == product_id).one()

        elif is_product_updated == 0:
            response_msg = "Product not updated. No product found with this id :" + \
                str(product_id)
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.delete("/{product_id}/delete")
async def delete_product(product_id: str):
    session = database.get_db_session(engine)
    try:
        is_product_updated = session.query(Product).filter(and_(Product.id == product_id, Product.deleted == False)).update({
            Product.deleted: True}, synchronize_session=False)
        session.flush()
        session.commit()
        response_msg = "Product deleted successfully"
        response_code = 200
        error = False
        data = {"product_id": product_id}
        if is_product_updated == 0:
            response_msg = "Product not deleted. No product found with this id :" + \
                str(product_id)
            error = True
            data = None
        return Response(data, response_code, response_msg, error)
    except Exception as ex:
        print("Error : ", ex)


@router.get("/{product_id}")
async def read_product(product_id: str):
    session = database.get_db_session(engine)
    response_message = "Product retrieved successfully"
    data = None
    try:
        data = session.query(Product).filter(
            and_(Product.id == product_id, Product.deleted == False)).one()
    except Exception as ex:
        print("Error", ex)
        response_message = "Product Not found"
    error = False
    return Response(data, 200, response_message, error)


@router.get("/")
async def read_all_products(created_by: str, page_size: int, page: int):
    session = database.get_db_session(engine)
    data = session.query(Product).filter(and_(Product.created_by == created_by, Product.deleted == False)).order_by(
        desc(Product.created_at)).limit(page_size).offset((page-1)*page_size).all()
    return Response(data, 200, "Products retrieved successfully.", False)
```

[endpoints/user.py](endpoints/user.py)
```python
from fastapi import APIRouter

# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_user():
    return {"name": "John", "email": "john@example.com"}
```

---

<div id="routes"></div>

## Create Routes

Now, let's create API routes:

[routes/api.py](routes/api.py)
```python
from fastapi import APIRouter
from endpoints import product, user

router = APIRouter()
router.include_router(product.router)
router.include_router(user.router)
```

---

<div id="main"></div>

## Implement main.py

Finally, let's implement main.py:

[main.py](main.py)
```python
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)
    print("running")
```

**NOTE:**  
Now just run **python main.py** to test.

---

**REFERENCES:**  
[Create REST API to perform CRUD Operations using FastAPI and MySQL](https://www.tutorialsbuddy.com/create-rest-api-to-perform-crud-operations-using-fastapi-and-mysql)  

---

**Rodrigo Leite -** *drigols*
