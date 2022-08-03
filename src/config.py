import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

FIXTURES_DIR = os.path.join(ROOT_DIR, "fixtures")

DATABASE_URL = os.environ["DATABASE_URL"]

TESTING_MODE = int(os.environ.get("TESTING", "0"))

TTL_SEARCH_IP = 30  # seconds

SRID_WGS84 = 4326
PRJ_ALBERS = (
    'PROJCS["Brazil / Albers Equal Area Conic (WGS84)",GEOGCS["WGS 84",'
    'DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,'
    'AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],'
    'PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],'
    'UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],'
    'AUTHORITY["EPSG","4326"]],PROJECTION["Albers_Conic_Equal_Area"],'
    'PARAMETER["longitude_of_center",-50.0],PARAMETER["standard_parallel_1",10.0],'
    'PARAMETER["standard_parallel_2",-40.0],PARAMETER["latitude_of_center",-25.0],'
    'UNIT["Meter",1.0]]'
)
