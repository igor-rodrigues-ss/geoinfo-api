from shapely.ops import transform
from shapely.wkt import loads as wkt_loads
from shapely.geometry import shape
from shapely.geometry.base import BaseGeometry

from pyproj import Transformer, CRS

from src.settings import PRJ_ALBERS, SRID_WGS84


class Geometry:

    _geom: BaseGeometry
    _reproj_geom: BaseGeometry

    def __init__(self, raw: str | dict):
        self._geom = self._load_geom(raw)
        self._reproj_geom = self._transform_geom(self._geom, SRID_WGS84, PRJ_ALBERS)

    def _load_geom(self, raw: str | dict) -> BaseGeometry:
        try:
            return wkt_loads(raw)
        except Exception:
            return shape(raw)

    def _to_km(self, meters: float) -> float:
        return round(meters / 1000, 2)

    def _transform_geom(self, geom, from_crs: int, to_crs: str) -> BaseGeometry:
        source_crs = CRS.from_epsg(from_crs)
        target_crs = CRS.from_wkt(to_crs)

        transformer = Transformer.from_crs(source_crs, target_crs)

        return transform(transformer.transform, geom)

    @property
    def geom_type(self) -> str:
        return self._geom.geom_type

    @property
    def wkt(self) -> str:
        return self._geom.wkt

    @property
    def area(self) -> float:
        return self._to_km(self._reproj_geom.area)

    @property
    def length(self) -> float:
        return self._to_km(self._reproj_geom.length)

    @property
    def centroid(self) -> dict:
        return self._geom.centroid.__geo_interface__
