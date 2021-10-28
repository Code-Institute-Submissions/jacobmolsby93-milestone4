from django.contrib import admin    
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'published', 'user')
    search_fields = ['title', 'content']
    list_filter = ('status', 'published', 'user')
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        queryset.update(approved=True)
