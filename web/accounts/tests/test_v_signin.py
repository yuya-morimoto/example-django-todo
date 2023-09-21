from django.test.client import Client
from django.urls import reverse


def test_get_status_200(client: Client) -> None:
    response = client.get(reverse("accounts:signin"))
    assert response.status_code == 200
