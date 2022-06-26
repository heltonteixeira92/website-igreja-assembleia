from django.urls import reverse
import pytest
from model_bakery import baker

from assembleiaproject.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('login'), follow=True)
    return resp


def test_status_code_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.senha_plana = password
    return user_model


@pytest.fixture
def resp_post(client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.senha_plana}, follow=True)


def test_status_code_login(resp_post):
    assert resp_post.status_code == 200


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
