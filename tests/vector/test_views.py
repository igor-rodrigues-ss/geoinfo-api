import json
import pytest

from unittest import mock
from http import HTTPStatus
from unittest.mock import MagicMock

from fastapi import status
from fastapi.testclient import TestClient as ClientTest

from tests.conftest import url_for


@pytest.mark.usefixtures("load_shapefile_data")
class TestViewsVectorInfo:
    @classmethod
    def setup_class(cls):
        cls.url = url_for("check-vector-info")

    def test_get_info_polygon(self, client: ClientTest):
        gj = {
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [[-50.92, -19.95], [-50.94, -20.06], [-50.85, -20.03], [-50.92, -19.95]]
                ],
            }
        }
        resp = client.post(self.url, data=json.dumps(gj))

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

    def test_get_info_linestring(self, client: ClientTest):
        gj = {
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-42.96, -21.59],
                    [-42.99, -21.77],
                    [-42.83, -22.13],
                    [-42.49, -22.15],
                ],
            }
        }
        resp = client.post(self.url, data=json.dumps(gj))

        assert resp.status_code == status.HTTP_200_OK

        data = resp.json()

        assert data["type"] == "LineString"
        assert data["length"] == pytest.approx(87.14)
        assert data["area"] == 0

        assert data["centroid"]["type"] == "Point"
        assert data["centroid"]["coordinates"] == pytest.approx([-42.83, -21.96], 0.01)
        assert data["locality"] == [
            {"acronym": "MG", "region": "Sudeste"},
            {"acronym": "RJ", "region": "Sudeste"},
        ]

    def test_get_info_point(self, client: ClientTest):
        gj = {
            "geometry": {
                "type": "Point",
                "coordinates": [-41.935665150025386, -21.63680829638541],
            }
        }
        resp = client.post("/vector/info", data=json.dumps(gj))

        assert resp.status_code == status.HTTP_200_OK

        data = resp.json()

        assert data["type"] == "Point"
        assert data["length"] == 0
        assert data["area"] == 0

        assert data["centroid"]["type"] == "Point"
        assert data["centroid"]["coordinates"] == pytest.approx([-41.93, -21.63], 0.01)
        assert data["locality"] == [
            {"acronym": "RJ", "region": "Sudeste"},
        ]

    @mock.patch("src.vector.views.Geometry")
    def test_get_info_error_500(self, m_Geometry: MagicMock, client: ClientTest):
        m_Geometry.side_effect = Exception("Fake Exception")

        payload = {
            "geometry": {
                "type": "Point",
                "coordinates": [-41.93, -21.63],
            }
        }
        resp = client.post(self.url, data=json.dumps(payload))

        assert resp.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

        data = resp.json()

        assert data["detail"] == HTTPStatus.INTERNAL_SERVER_ERROR.phrase
