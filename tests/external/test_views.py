from unittest import mock
from unittest.mock import MagicMock, AsyncMock

from fastapi import status
from fastapi.testclient import TestClient as ClientTest


class TestViewsSearchIP:
    @mock.patch("src.external.views.client", new_callable=AsyncMock)
    def test_search_ip_success(self, m_client: AsyncMock, client: ClientTest):
        search_ip = "192.168.10.12"
        expected = {
            "hostname": "192-168-10-12.user3p.brasiltelecom.net.br",
            "country": "BR",
            "region": "Goiás",
            "city": "Goiania",
            "loc": "-16.704872,-49.474467",
            "org": "AS7018 AT&T Services, Inc.",
            "bogon": False,
        }
        m_resp = MagicMock()
        m_resp.json.return_value = {"ip": search_ip, **expected}
        m_client.get.return_value = m_resp

        response = client.get(f"/external/ip?address={search_ip}")

        assert response.status_code == status.HTTP_200_OK
        assert m_client.get.call_count == 1
        assert response.json() == expected

        response = client.get(f"/external/ip?address={search_ip}")

        assert response.status_code == status.HTTP_200_OK
        assert m_client.get.call_count == 1
        assert response.json() == expected

    def test_search_ip_bad_request(self, client: ClientTest):
        response = client.get("/external/ip?address=xyzabc")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
