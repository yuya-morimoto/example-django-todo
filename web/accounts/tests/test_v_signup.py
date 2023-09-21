import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse


def test_get_status_200(client: Client) -> None:
    response = client.get(reverse("accounts:signup"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_status_302(client: Client) -> None:
    response = client.post(
        path=reverse("accounts:signup"),
        data={"username": "testuser", "password1": "testpass1111", "password2": "testpass1111"},
    )
    created_user = User.objects.get(username="testuser")
    assert created_user.username == "testuser"
    assert response.status_code == 302
