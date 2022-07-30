import sys

from yoyo import read_migrations
from yoyo import get_backend


def apply(database_url: str):
    backend = get_backend(database_url)
    migrations = read_migrations("./migrations")
    backend.apply_migrations(backend.to_apply(migrations))


if __name__ == "__main__":
    apply(sys.argv[1])
