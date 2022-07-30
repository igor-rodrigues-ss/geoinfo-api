from pydantic import BaseModel


class InfoRequestSchema(BaseModel):
    geometry: str

    class Config:
        schema_extra = {"example": {"geometry": "POINT (1 1)"}}


class InfoResponseSchema(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "type": "",
                "length": 0.0,
                "area": 0.0,
                "centroid": {"lat": 0.0, "lng": 0.0},
                "locality": [
                    {"country": "", "region": "", "city": ""},
                    {"country": "", "region": "", "city": ""},
                    {"country": "", "region": "", "city": ""},
                ],
            }
        }
