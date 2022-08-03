from cachecall import cache

from src.external.schemas import SeachIPResponseSchema
from src.external.helper.client import client
from src.external.helper.validator import validate_ip
from src.config import TTL_SEARCH_IP


@cache(ttl=TTL_SEARCH_IP)
async def search_ip(address: str) -> SeachIPResponseSchema:
    validate_ip(address)

    resp = await client.get(f"https://ipinfo.io/{address}/geo")

    return SeachIPResponseSchema(**resp.json())
