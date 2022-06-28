from django.shortcuts import render, get_object_or_404

# Create your views here.
from assembleiaproject.gallery.models import Image


def gallery(request):
    return render(request, 'gallery.html')


def photo_detail(request, slug):
    photo = get_object_or_404(Image, slug=slug)
    context = {'photo': photo}
    return render(request, '', context)
