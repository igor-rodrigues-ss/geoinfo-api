import json
import pytest

from fastapi import status


@pytest.mark.usefixtures("load_shapefile_data")
class TestVectorInfo:
    def test_get_info_polygon(self, client):
        gj = {
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [[-50.92, -19.95], [-50.94, -20.06], [-50.85, -20.03], [-50.92, -19.95]]
                ],
            }
        }
        resp = client.post("/vector/info", data=json.dumps(gj))

        assert resp.status_code == status.HTTP_200_OK

        data = resp.json()

        assert data["type"] == "Polygon"
        assert data["length"] == pytest.approx(27.51)
        assert data["area"] == pytest.approx(36392.62)

        assert data["centroid"]["type"] == "Point"
        assert data["centroid"]["coordinates"] == pytest.approx([-50.90333333, -20.01333333])
        assert data["locality"] == [
            {"acronym": "MG", "region": "Sudeste"},
            {"acronym": "SP", "region": "Sudeste"},
        ]

    @pytest.mark.skip("Must be implemented")
    def test_get_info_linestring(self, client):
        pass

    @pytest.mark.skip("Must be implemented")
    def test_get_info_point(self, client):
        pass
