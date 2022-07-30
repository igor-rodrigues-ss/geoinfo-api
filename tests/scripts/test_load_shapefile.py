import pytest

from sqlalchemy import func
from sqlalchemy.future import select

from scripts.load_shapefile import load_shapefile
from tests.conftest import get_file_from_fixtures

from src.db import Session
from src.vector.models import BrUf


@pytest.mark.asyncio
async def test_load_shapefile():
    await load_shapefile(get_file_from_fixtures("southeast.zip"))

    async with Session() as sess:
        query = select(func.count(BrUf.id))
        result = await sess.execute(query)
        ufs_count = result.scalar()

    assert ufs_count == 4
