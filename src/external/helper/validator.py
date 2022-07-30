from ipaddress import ip_address

from fastapi import status
from fastapi import HTTPException


def validate_ip(address: str):
    try:
        ip_address(address)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
