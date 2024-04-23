# from __future__ import annotations#

from typing import Annotated, List

from fastapi import APIRouter, Depends

from repository import ProductRepository
from schemas import ProductAdd, Product

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


# http://127.0.0.1:8000/docs#/default/
@router.post("")
async def add_product(
        product: Annotated[ProductAdd, Depends()],
) -> dict:
    product_id = await ProductRepository.add_product(product)
    return {"ok": True, "product_id": product_id}


@router.post("{product_id}")
async def change_product_amount(
        product_id: int,
        new_amount: str,
) -> Product | dict:
    products = await ProductRepository.find_products()

    if product_id and new_amount:
        current_product = next((product for product in products if product.id == product_id), None)
        if current_product:
            current_product = Product(id=current_product.id, name=current_product.name, amount=new_amount)
            return current_product

    return {'error': 'You wrote not existed id.'}


@router.get("")
async def get_products() -> List[Product]:
    products = await ProductRepository.find_products()
    return products
