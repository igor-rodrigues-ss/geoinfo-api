from typing import Dict

from sqlalchemy import Column, String, Integer, text
from sqlalchemy.future import select
from geoalchemy2 import Geometry

from src.db import Session, Base


class BrUf(Base):
    __tablename__ = "br_uf"
    id = Column(Integer, primary_key=True)
    cd_uf = Column(String)
    nm_uf = Column(String)
    sigla = Column(String(length=4))
    nm_regiao = Column(String)
    geometry = Column(Geometry(srid=4674))

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

    @classmethod
    async def locality(cls, geom_wkt: str) -> Dict[str, str]:
        async with Session() as sess:
            stmt = text(
                """
            WITH ufs AS (
                SELECT
                    sigla, nm_regiao
                FROM
                    br_uf
                WHERE
                    ST_Intersects(ST_GeomFromText(:geom), "geometry")
                ORDER BY
                    sigla
            ),
            jdata AS (
                SELECT
                    json_build_object(
                        'acronym', ufs.sigla,
                        'region', ufs.nm_regiao
                    ) AS uf
                FROM ufs
            )
            SELECT ARRAY_AGG(uf) AS locality FROM jdata;
            """
            )
            result = await sess.execute(stmt, {"geom": geom_wkt})
            return dict(result.fetchone())
