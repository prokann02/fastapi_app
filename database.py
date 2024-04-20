from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

database = create_async_engine(
    "sqlite+aiosqlite:///products.db"
)

new_session = async_sessionmaker(database, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class ProductsTable(Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    amount: Mapped[str]


async def create_tables():
    async with database.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with database.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
