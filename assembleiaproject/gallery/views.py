from django.shortcuts import render, get_object_or_404

# Create your views here.
from assembleiaproject.gallery.models import Image, Album # noqa


def gallery(request):
    photos = Image.photopublished.all()

    context = {'photos': photos,
               'section': 'gallery'
               }

    # Album.objects.select_related()
    return render(request, 'gallery.html', context)


def photo_detail(request, slug):
    photo = get_object_or_404(Image, slug=slug)
    context = {'photo': photo}
    return render(request, '', context)
