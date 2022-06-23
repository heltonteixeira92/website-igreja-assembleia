import pytest # noqa
from django.urls import reverse # noqa
from assembleiaproject.blog.models import Post

# @pytest.fixture
# def resp(client, post_created):
#     resp = client.get(reverse('blog:post_detail', args=[post_created.publish.year,
#                                                         post_created.publish.month,
#                                                         post_created.publish.day,
#                                                         post_created.slug]))
#
#
# def test_status_code(resp):
#     assert resp.status_code == 200


def test_post_created(post_created):
    assert isinstance(post_created, Post)
