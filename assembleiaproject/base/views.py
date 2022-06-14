from django.shortcuts import render

from assembleiaproject.blog.models import Post


def home(request):
    posts = Post.published.all()[:3]
    context = {'posts': posts}
    return render(request, 'home.html', context)
