from django.contrib import admin

from Tags.models import Tag


# Register your models here.


class TagAdmin(admin.ModelAdmin):
    fields = ['tag_name', 'posts', ]


admin.site.register(Tag, TagAdmin)
