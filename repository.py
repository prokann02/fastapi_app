from typing import List

from sqlalchemy import select

from database import new_session, ProductsTable
from schemas import ProductAdd, Product


class ProductRepository:
    @classmethod
    async def add_product(cls, data: ProductAdd) -> int:
        async with new_session() as session:
            # Convert to dict
            product_dict = data.model_dump()

            product = ProductsTable(**product_dict)
            session.add(product)

            # Make it to get id
            await session.flush()

            # Send to database
            await session.commit()
            return product.id

    @classmethod
    async def find_products(cls) -> List[Product]:
        async with new_session() as session:
            query = select(ProductsTable)
            result = await session.execute(query)

            # Scalars: each row is represented by a single value instead of a tuple
            product_models = result.scalars().all()

            # Convert each row to a dictionary
            product_dicts = []
            for product_model in product_models:
                product_dict = {
                    column.name: getattr(product_model, column.name)
                    for column in ProductsTable.__table__.columns
                }
                product_dicts.append(product_dict)

            # Validate the dictionaries as instances of Product
            product_schemas = [Product(**product_dict) for product_dict in product_dicts]

            return product_schemas
