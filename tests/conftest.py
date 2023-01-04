import os

from tests.db import Database

database_test = Database()


from src.main import app
from src.db import Session
from src.config import ROOT_DIR
from scripts.apply import apply
from src.vector.models import BrUf


pytest_plugins = ["tests.base_fixtures"]


def get_file_from_fixtures(fname: str) -> str:
    return os.path.join(ROOT_DIR, "tests", "fixtures", fname)


def url_for(name: str) -> str:
    return app.url_path_for(name)


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
