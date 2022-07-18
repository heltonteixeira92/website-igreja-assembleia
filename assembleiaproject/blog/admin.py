from django.contrib import admin
# from django.urls import reverse

from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    # exclude = 'slug',

    # @staticmethod
    # def view_on_site(obj):
    #     return reverse('blog:post_detail', kwargs={'year': obj.publish.year, 'month': obj.publish.month,
    #                                                'post': obj.slug})

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
