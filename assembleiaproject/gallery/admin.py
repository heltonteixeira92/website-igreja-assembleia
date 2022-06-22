from django.contrib import admin
from .models import Image, Album


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'img', 'created')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created', )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
