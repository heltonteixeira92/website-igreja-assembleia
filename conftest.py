import pytest
from model_bakery import baker


def gen_func():
    return 'value'


baker.generators.add('ckeditor.fields.RichTextField', gen_func)


@pytest.fixture
def post_created(db):
    post_model = baker.make('Post')
    return post_model


@pytest.fixture
def user_logged_in(db, django_user_model):
    user_model = baker.make(django_user_model, first_name='Fulano')
    return user_model


@pytest.fixture
def client_with_user_logged_in(user_logged_in, client):
    client.force_login(user_logged_in)
    return client
