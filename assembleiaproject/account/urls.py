from django.urls import path
from .views import user_login, activate_user, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('activate-user/<uidb64>/<token>', activate_user, name='activate'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
