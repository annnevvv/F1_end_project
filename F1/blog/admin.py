from django.contrib import admin

# Register your models here.

from .models import Author, Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags')
    list_display = ('title', 'author', 'date')
    # prepopulated_fields = {'slug': ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('post',)
    list_display = ('user_name', 'user_email')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
