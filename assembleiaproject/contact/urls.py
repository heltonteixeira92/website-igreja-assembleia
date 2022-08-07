from django.urls import path
from .views import contact_us, get_message


app_name = 'contact'

urlpatterns = [
    path('', contact_us, name='contact_us'),
    path('message/', get_message, name='get_message')
]
