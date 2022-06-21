from django.shortcuts import render

from assembleiaproject.blog.models import Post
from assembleiaproject.contact.models import Message


def home(request):
    posts = Post.published.all()[:3]
    context = {'posts': posts}
    return render(request, 'home.html', context)


def contact_us(request):
    name = request.POST.get('name')
    email = request.POST.get('emailAddress')
    message = request.POST.get('message')
    Message.objects.create(
        name=name,
        email=email,
        message=message
    )
    return render(request, 'contact-us.html')


def about_us(request):
    return render(request, 'about-us.html')
