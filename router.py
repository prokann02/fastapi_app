from typing import Annotated, List

from fastapi import APIRouter, Depends

from repository import ProductRepository
from schemas import ProductAdd, Product, ProductId

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# http://127.0.0.1:8000/docs#/default/
@router.post("")
async def add_product(
        product: Annotated[ProductAdd, Depends()],
) -> ProductId:
    product_id = await ProductRepository.add_product(product)
    return {"ok": True, "product_id": product_id}


@router.get("")
async def get_products() -> List[Product]:
    products = await ProductRepository.find_products()
    return products
