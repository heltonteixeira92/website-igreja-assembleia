from django.test import Client
from django.urls import reverse
import pytest


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'), follow=True)
    return resp

# emula requisição http
def test_status_code(resp):
    assert resp.status_code == 200
