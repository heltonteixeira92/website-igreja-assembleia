from django.urls import reverse
import pytest


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:contato'), follow=True)
    return resp


# def test_status_code(resp):
#     assert resp.status_code == 200
