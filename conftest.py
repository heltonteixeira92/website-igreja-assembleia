import pytest
from model_bakery import baker


@pytest.fixture
def post_created(db):
    post_model = baker.make('Post')
    return post_model
