from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostInline(admin.StackedInline):
    model = Comments
    extra = 1
    exclude = ('comments_date',)
    readonly_fields = ('comments_date',)


class PostAdmin(SummernoteModelAdmin):
    exclude = ('post_stars', 'post_date')
    readonly_fields = ('post_stars', 'post_date')
    inlines = [PostInline]


admin.site.register(Post, PostAdmin)
