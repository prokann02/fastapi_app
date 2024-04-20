from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from logging_settings import set_logging
from router import router as products_router


logging = set_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    logging.info("\t  Database wac cleaned")

    await create_tables()
    logging.info("\t  Database is ready")

    yield
    logging.info("\t  Turning off")


app = FastAPI(lifespan=lifespan)
app.include_router(products_router)
