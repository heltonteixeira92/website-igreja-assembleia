from django.urls import reverse
import pytest
from assembleiaproject.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('login'), follow=True)
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_button_join(resp):
    assert_contains(resp, 'Entrar')


def test_input_email(resp):
    assert_contains(resp, '<label class="form-label" for="form1Example13">Email</label>')


def test_input_password(resp):
    assert_contains(resp, '<label class="form-label" for="form1Example23">Senha</label>')


@pytest.fixture
def resp_with_user_logged_in(client_with_user_logged_in, db):
    return client_with_user_logged_in.get(reverse('base:home'), follow=True)


def test_link_login_unavailable(resp_with_user_logged_in):
    assert_not_contains(resp_with_user_logged_in, 'Entrar')
