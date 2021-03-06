from django import template
from ..models import Post

register = template.Library()


@register.simple_tag()
def total_posts():
    return Post.published.count()


@register.inclusion_tag('post/latest_posts.html')
def shoow_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
