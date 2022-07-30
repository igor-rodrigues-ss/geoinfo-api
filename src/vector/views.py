from src.vector.schemas import InfoRequestSchema


async def info(body: InfoRequestSchema):
    return {
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
