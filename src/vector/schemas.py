from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class InfoRequestSchema(BaseModel):
    geometry: str | Dict[Any, Any]

    class Config:
        schema_extra = {
            "example": {
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [[-50.92, -19.95], [-50.94, -20.06], [-50.85, -20.03], [-50.92, -19.95]]
                    ],
                }
            }
        }


class InfoResponseSchema(BaseModel):
    type: str
    length: float
    area: float
    centroid: Dict[Any, Any]
    locality: Optional[List[Dict[str, str]]]

    class Config:
        schema_extra = {
            "example": {
                "type": "Polygon",
                "length": 27.51,
                "area": 36392.62,
                "centroid": {
                    "type": "Point",
                    "coordinates": [-50.903333333333336, -20.013333333333332],
                },
                "locality": [
                    {"acronym": "MG", "region": "Sudeste"},
                    {"acronym": "SP", "region": "Sudeste"},
                ],
            }
        }
