from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_on', 'updated_on',)
    list_filter = ('published_on',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author',)
