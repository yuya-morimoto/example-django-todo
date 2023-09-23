from django.test.client import Client
from django.urls import reverse


def test_status_200(client: Client) -> None:
    response = client.get(reverse("accounts:index"))
    assert response.status_code == 200
