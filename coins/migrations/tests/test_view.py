import pytest

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

@pytest.fixture
def client():
    return APIClient()


class TestCoinsView:
    def test_coins_view_status(self, client):
        url = reverse('coins:coins-detail')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
