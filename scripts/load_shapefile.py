import os
import json
import shapefile

from typing import Optional
from zipfile import ZipFile
from tempfile import TemporaryDirectory

from src.config import FIXTURES_DIR
from src.vector.models import BrUf


async def load_shapefile(path: Optional[str] = None):
    if not path:
        path = os.path.join(FIXTURES_DIR, "BR_UF_2021.zip")

    tmpdir = _extract_files(path)

    shp_path = _find_shp(tmpdir.name)

    await _import_shp(shp_path)

    tmpdir.cleanup()


def _extract_files(path: str) -> TemporaryDirectory:
    tmpdir = TemporaryDirectory()

    with ZipFile(path) as zipf:
        zipf.extractall(tmpdir.name)

    return tmpdir


def _find_shp(directory: str) -> str:
    for fname in os.listdir(directory):
        if fname.endswith(".shp"):
            return os.path.join(directory, fname)

    raise FileNotFoundError(".shp file not found.")


async def _import_shp(path: str):
    shp_reader = shapefile.Reader(path)

    for feature in shp_reader:
        properties = feature.record.as_dict()
        geometry = feature.shape.__geo_interface__

        await BrUf(
            cd_uf=properties["CD_UF"],
            nm_uf=properties["NM_UF"],
            sigla=properties["SIGLA"],
            nm_regiao=properties["NM_REGIAO"],
            geometry=json.dumps(geometry),
        ).save()
