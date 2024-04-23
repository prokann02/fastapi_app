from pydantic import BaseModel, Field


class ProductAdd(BaseModel):
    name: str  # For example: Apples
    amount: str = Field(max_length=10)  # For example: 3 kg


class Product(ProductAdd):
    id: int


class ProductId(BaseModel):
    ok: bool = True
    product_id: int
