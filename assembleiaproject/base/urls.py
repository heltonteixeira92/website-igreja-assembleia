from django.urls import path
from assembleiaproject.base.views import home, about_us

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('sobre-nos', about_us, name='about_us'),
]
