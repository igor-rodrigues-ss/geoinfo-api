import pytest

from unittest import mock
from typing import Generator

from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="session", autouse=True)
def mock_load_shapefile():
    with mock.patch("src.main.load_shapefile", new_callable=mock.AsyncMock):
        yield


@pytest.fixture(scope="session")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app, raise_server_exceptions=False) as tc:
        yield tc
