import os
import pytest

from tests.db import Database

database_test = Database()

from scripts.apply import apply
from scripts.load_shapefile import load_shapefile

from src.vector.models import BrUf
from src.db import Session
from src.config import ROOT_DIR


pytest_plugins = ["tests.plugins.base_fixtures"]


def get_file_from_fixtures(fname: str) -> str:
    return os.path.join(ROOT_DIR, "tests", "fixtures", fname)


def pytest_sessionstart(session):
    print("Apply migrations...")
    apply(database_test.postgresql.url())
    print("Successful.")


def pytest_sessionfinish(session, exitstatus):
    database_test.stop()


async def truncate_br_uf():
    async with Session() as sess:
        await sess.execute(f"TRUNCATE TABLE {BrUf.__tablename__}")
        await sess.commit()


@pytest.fixture
async def load_shapefile_data():
    await load_shapefile(get_file_from_fixtures("southeast.zip"))

    yield

    await truncate_br_uf()
