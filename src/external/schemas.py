from pydantic import BaseModel
from typing import Optional


class SeachIPResponseSchema(BaseModel):
    hostname: Optional[str]
    country: Optional[str]
    region: Optional[str]
    city: Optional[str]
    loc: Optional[str]
    org: Optional[str]
    bogon: Optional[bool] = False

    class Config:
        schema_extra = {
            "example": {
                "hostname": "192-168-10-12.user3p.brasiltelecom.net.br",
                "country": "BR",
                "region": "Goiás",
                "city": "Goiania",
                "loc": "-16.704872,-49.474467",
                "org": "AS7018 AT&T Services, Inc.",
                "bogon": False,
            }
        }
