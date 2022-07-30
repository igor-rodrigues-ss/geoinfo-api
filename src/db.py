import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


def create_engine():
    pool_custom_config = {}

    if int(os.environ.get("TESTING", "0")) == 1:
        pool_custom_config = {"poolclass": NullPool}

    return create_async_engine(
        os.environ.get("DATABASE_URL", "").replace("postgresql", "postgresql+asyncpg"),
        **pool_custom_config,
    )


Base = declarative_base()
engine = create_engine()
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
