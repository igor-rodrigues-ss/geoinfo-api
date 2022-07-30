from src.external.schemas import SeachIPResponseSchema
from src.external.helper.client import client
from src.external.helper.validator import validate_ip


async def search_ip(address: str) -> SeachIPResponseSchema:
    validate_ip(address)

    resp = await client.get(f"https://ipinfo.io/{address}/geo")

    return SeachIPResponseSchema(**resp.json())
