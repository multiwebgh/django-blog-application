from django.contrib import admin
from .models import Blog,Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Blog, BlogAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'comment', 'created_at')
admin.site.register(Comment, CommentAdmin)
