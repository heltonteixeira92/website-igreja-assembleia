from django.urls import path
from assembleiaproject.base.views import home, contact_us

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('contato', contact_us, name='contato'),
]
