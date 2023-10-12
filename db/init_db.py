from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .models import Base

from config import db_url


#Database connection
engine = create_async_engine(db_url, echo=True)
async_session = async_sessionmaker(engine,
                                   expire_on_commit=False)


# Create database
async def start_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)