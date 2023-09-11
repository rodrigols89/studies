from fastapi import APIRouter
from endpoints import product

apiRouter = APIRouter()

# Add product router.
apiRouter.include_router(product.productRouterSettings)
