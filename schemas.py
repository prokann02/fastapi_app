from pydantic import BaseModel


class ProductAdd(BaseModel):
    name: str  # For example: Apples
    amount: str  # For example: 3 kg


class Product(ProductAdd):
    id: int


class ProductId(BaseModel):
    ok: bool = True
    product_id: int
