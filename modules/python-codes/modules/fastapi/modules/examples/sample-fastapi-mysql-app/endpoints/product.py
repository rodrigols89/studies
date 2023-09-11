from fastapi import APIRouter

from schemas.request import ProductRequest

from models.product import Product

from db.database import Database
from sqlalchemy import and_, desc

database = Database()
engine = database.get_db_connection()

# APIRouter creates path operations for product module
productRouterSettings = APIRouter(
    prefix="/products",
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)

@productRouterSettings.post("/add", response_description="Product data added into the database")
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
