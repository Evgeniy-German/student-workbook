from django.contrib.auth.models import User
from django.db import models
from star_ratings.models import Rating


# Create your models here.


class Post(models.Model):
    class Meta:
        db_table = 'post'

    post_title = models.CharField(max_length=100)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_short_description = models.CharField(max_length=100)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField()
    comments_date = models.DateTimeField(auto_now_add=True)
    comments_parent = models.IntegerField(default=0)
    comments_likes = models.ManyToManyField(User, related_name='like')
    comments_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comments_author = models.ForeignKey(User, on_delete=models.CASCADE)
