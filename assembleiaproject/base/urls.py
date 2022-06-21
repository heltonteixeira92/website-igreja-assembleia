from django.urls import path
from assembleiaproject.base.views import home, contact_us, about_us

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('contato', contact_us, name='contato'),
    path('sobre-nos', about_us, name='about_us'),
]
