from django.shortcuts import render
from Post.models import Post
from Tags.models import Tag


# Create your views here.

def show_posts_by_teg(request, tag_value):
    tag = Tag.objects.get(id=tag_value)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'home/Posts_by_tag.html', {'posts': posts, 'tag': tag})
