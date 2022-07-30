import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

FIXTURES_DIR = os.path.join(ROOT_DIR, "fixtures")

DATABASE_URL = os.environ["DATABASE_URL"]

TESTING_MODE = int(os.environ.get("TESTING", "0"))
