from django.test import Client


# emula requisição http
def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
