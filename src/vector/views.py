from src.vector.schemas import InfoRequestSchema
from src.vector.geometry import Geometry
from src.vector.models import BrUf


async def info(body: InfoRequestSchema):
    geom = Geometry(body.geometry)
    locality = await BrUf.locality(geom.wkt)

    return {
        "type": geom.geom_type,
        "length": geom.length,
        "area": geom.area,
        "centroid": geom.centroid,
        **locality,
    }
