from django.urls import path
from assembleiaproject.gallery.views import gallery, photo_detail

app_name = 'gallery'

urlpatterns = [
    path('', gallery, name='gallery'),
    path('imagem/<slug:slug>/', photo_detail, name='photo_detail')
]
