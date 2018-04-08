from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Comments


# Register your models here.
class PostInline(admin.StackedInline):
    model = Comments
    extra = 1
    exclude = ('comments_date', 'comments_likes')
    readonly_fields = ('comments_date', 'comments_likes')


class PostAdmin(SummernoteModelAdmin):
    exclude = ('post_date', 'post_date_update', )
    readonly_fields = ('post_date', 'post_date_update',)
    inlines = [PostInline]


admin.site.register(Post, PostAdmin)
