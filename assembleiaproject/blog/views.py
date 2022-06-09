from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    context = {'posts': posts}

    return render(request, '', context)


def post_detail(request, day, year, month, post):
    post = get_object_or_404(Post, slug=post,
                             status='publised',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post': post}
    return render(request, '', context)
