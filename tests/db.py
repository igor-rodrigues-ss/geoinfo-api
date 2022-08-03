import os
import testing.postgresql


class Database:
    def __init__(self):
        print("Starting database...")

        self.postgresql = testing.postgresql.Postgresql()
        os.environ["DATABASE_URL"] = self.postgresql.url()

        print("Successful.")

    def stop(self):
        self.postgresql.stop()
