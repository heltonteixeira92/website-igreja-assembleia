from django.urls import path
from assembleiaproject.gallery.views import gallery

app_name = 'gallery'

urlpatterns = [
    path('', gallery, name='gallery'),
]
