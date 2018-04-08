from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'post_short_description', 'tags', 'post_speciality_number']
        widgets = {
            'post_text': SummernoteWidget,
        }
