from django.shortcuts import render

from assembleiaproject.blog.models import Post
from assembleiaproject.contact.models import Message
from assembleiaproject.gallery.models import Image


def home(request):
    posts = Post.published.all()[:6]
    photos = Image.photopublished.all()[:6]
    context = {'posts': posts,
               'photos': photos,
               'section': 'home',
               }
    return render(request, 'home.html', context)


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('emailAddress')
        message = request.POST.get('message')
        Message.objects.create(
            name=name,
            email=email,
            message=message
        )
    context = {'section': 'contact_us'}
    return render(request, 'contact-us.html', context)


def about_us(request):
    context = {'section': 'about_us'}
    return render(request, 'about-us.html', context)


def handler500(request):
    response = render(request, 'errors/error-500.html')
    response.status_code = 500
    return response


def handler404(request, exception):
    response = render(request, 'errors/error-404.html')
    response.status_code = 404
    return response
