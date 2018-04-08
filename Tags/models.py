from django.db import models

# Create your models here.



class Tag(models.Model):
    class Meta:
        db_table = 'tag'

    tag_name = models.CharField(max_length=15)
    posts = models.ManyToManyField('Post.Post', blank=True)

    def __str__(self):
        return self.tag_name
