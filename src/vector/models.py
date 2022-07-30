from sqlalchemy import Column, String, Integer
from geoalchemy2 import Geometry
from sqlalchemy.future import select

from src.db import Session, Base


class BrUf(Base):
    __tablename__ = "br_uf"
    id = Column(Integer, primary_key=True)
    cd_uf = Column(String)
    nm_uf = Column(String)
    sigla = Column(String(length=4))
    nm_regiao = Column(String)
    geometry = Column(Geometry())

    async def save(self):
        async with Session() as sess:
            sess.add(self)
            await sess.commit()

    @classmethod
    async def exists(cls) -> bool:
        async with Session() as sess:
            stmt = select(cls).limit(1)
            result = await sess.execute(stmt)

        return bool(result.scalar())
