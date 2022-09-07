from django.urls import reverse
import pytest
from assembleiaproject.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'), follow=True)
    return resp


# emula requisição http
def test_status_code(resp):
    assert resp.status_code == 200


def test_entry_button(resp):
    assert_contains(resp, 'Login')


def test_gallery_button(resp):
    assert_contains(resp, 'galeria')


def test_blog_button(resp):
    assert_contains(resp, 'blog')


# def test_gallery_section_title_home(resp):
#    assert_contains(resp, '<h1 class="fw-light text-center text-lg-start mt-4 mb-0">Galeria</h1>')


def test_post_section_title_home(resp):
    assert_contains(resp, '<h1 class="fw-light text-center text-lg-start mt-4 mb-0">Postagens Recentes</h1>')
