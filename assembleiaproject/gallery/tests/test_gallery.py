import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('gallery:gallery'), follow=True)
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
