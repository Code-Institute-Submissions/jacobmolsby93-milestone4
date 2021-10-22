from django.contrib import admin
from .models import Article
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'published', 'user')
    search_fields = ['title', 'content']
    list_filter = ('status', 'published', 'user')
    summernote_fields = ('content')
