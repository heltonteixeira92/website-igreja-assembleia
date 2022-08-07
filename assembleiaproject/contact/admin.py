from django.contrib import admin
from .models import Message


# Register your models here.
@admin.register(Message)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
