import os

import testing.postgresql

from scripts.apply import apply

print("Starting database...")

postgresql = testing.postgresql.Postgresql()
os.environ["DATABASE_URL"] = postgresql.url()

print("Successful.")

from src.config import ROOT_DIR

pytest_plugins = ["tests.plugins.base_fixtures"]


def get_file_from_fixtures(fname: str) -> str:
    return os.path.join(ROOT_DIR, "tests", "fixtures", fname)


def pytest_sessionstart(session):
    print("Apply migrations...")
    apply(postgresql.url())
    print("Successful.")


def pytest_sessionfinish(session, exitstatus):
    postgresql.stop()
