from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from src.config import DATABASE_URL, TESTING_MODE


def create_engine():
    pool_custom_config = {}

    if TESTING_MODE == 1:
        pool_custom_config = {"poolclass": NullPool}

    return create_async_engine(
        DATABASE_URL.replace("postgresql", "postgresql+asyncpg"),
        **pool_custom_config,
    )


Base = declarative_base()
engine = create_engine()
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
