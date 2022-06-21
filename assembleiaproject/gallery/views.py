from django.shortcuts import render # noqa

# Create your views here.


def gallery(request):
    return render(request, 'gallery.html')
