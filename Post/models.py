from datetime import datetime
from django.db import models


# Create your models here.

class Post(models.Model):
    class Meta():
        db_table = 'post'

    post_title = models.CharField(max_length = 100)
    post_text = models.TextField()
    post_date = models.DateField()
    post_stars = models.IntegerField(default = 0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.post_date = datetime.now()


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_date = models.DateField()
    comments_parent = models.IntegerField(default = 0)
    comments_post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.comments_date = datetime.now()
