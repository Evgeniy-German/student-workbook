from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from Post.models import Post, Comments


# Create your views here.


def post(request, post_id):
    return render(request, 'home/post.html', {'post': Post.objects.get(id=post_id),
                                              'comments': Comments.objects.filter(comments_post_id=post_id)})


def addlike(request, post_id, comment_id):
    try:
        user = request.user
        comment = Comments.objects.get(id=comment_id)
        if user in comment.comments_likes.all():
            comment.comments_likes.remove(user)
        else:
            comment.comments_likes.add(user)
        comment.save()
    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect('/' + str(post_id))
