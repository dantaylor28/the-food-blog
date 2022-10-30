from django.contrib import admin
from .models import Post, Comment, Label, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'published_on', 'updated_on',)
    list_filter = ('published_on',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author',)
    summernote_fields = ('body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'name', 'date_commented',)
    list_filter = ('date_commented',)
    search_fields = ('name', 'post',)


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
