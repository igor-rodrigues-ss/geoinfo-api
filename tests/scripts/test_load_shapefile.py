import pytest

from sqlalchemy import func
from sqlalchemy.future import select

from scripts.load_shapefile import load_shapefile
from tests.conftest import get_file_from_fixtures, truncate_br_uf

from src.db import Session
from src.vector.models import BrUf


@pytest.fixture
async def setup_teardown():
    await truncate_br_uf()
    yield
    await truncate_br_uf()


@pytest.mark.usefixtures("setup_teardown")
async def test_load_success():
    await load_shapefile(get_file_from_fixtures("southeast.zip"))

    async with Session() as sess:
        query = select(func.count(BrUf.id))
        result = await sess.execute(query)
        ufs_count = result.scalar()

    assert ufs_count == 4
