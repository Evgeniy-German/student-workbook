from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from Post.forms import PostForm
from Post.models import Post, Comments


# Create your views here.


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comments.objects.filter(comments_post_id=post_id)
    form = PostForm(instance=post)
    return render(request, 'home/post.html', {'post': post,
                                              'comments': comments,
                                              'form': form}
                  )


def addlike(request, post_id, comment_id):
    try:
        user = request.user
        comment = Comments.objects.get(id=comment_id)
        if user.is_authenticated:
            if user in comment.comments_likes.all():
                comment.comments_likes.remove(user)
            else:
                comment.comments_likes.add(user)
            comment.save()
    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect('/' + str(post_id))


def my_profile(request):
    if request.method == 'POST':
        return delete_post(request)
    elif request.user.is_authenticated:
        posts = Post.objects.filter(post_author=request.user)
        return render(request, 'home/MyProfile.html', {'posts': reversed(posts)})
    else:
        return HttpResponseRedirect('/')


def create_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.post_short_description = form.cleaned_data['post_short_description']
            post.post_text = form.cleaned_data['post_text']
            post.post_title = form.cleaned_data['post_title']
            post.post_author = request.user
            post.save()
            return HttpResponseRedirect('/MyProfile/')
    else:
        form = PostForm()
    return render(request, 'home/EditPost.html', {'form': form})


def edit_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST' and user.is_authenticated and post.post_author == user:
        post.post_title = request.POST['post_title']
        post.post_text = request.POST['post_text']
        post.post_short_description = request.POST['post_short_description']
        form = PostForm(instance=post)
        post.save()
        return render(request, 'home/EditPost.html', {'form': form, 'good_news': 'True'})
    elif user.is_authenticated:
        form = PostForm(instance=post)
        return render(request, 'home/EditPost.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


def delete_post(request):
    user = request.user
    post = get_object_or_404(Post, id=request.POST['delete_post'])
    if user.is_authenticated and post.post_author == user:
        post.delete()
        return HttpResponseRedirect('/MyProfile/')
    else:
        return render(request, 'home/home.html')


def add_comment(request):
    text = request.POST['text']
    count = int(request.POST['count'])
    post_id = request.POST['post_id']
    if text:
        user = request.user
        comment = Comments()
        comment.comments_author = user
        comment.comments_post_id = post_id
        comment.comments_text = text
        comment.save()
        answer_dict = {'text': comment.comments_text, 'author': user.username, 'date': comment.comments_date,
                       'post_id': post_id, 'comments_id': comment.id, 'coments_like': comment.comments_likes.count()}
        return JsonResponse(answer_dict)
    elif Comments.objects.filter(comments_post_id=post_id).count() != count:
        comment = Comments.objects.filter(comments_post_id=post_id)
        comment = comment[count:count + 1]
        comment = comment[0]
        user = comment.comments_author
        answer_dict = {'text': comment.comments_text, 'author': user.username, 'date': comment.comments_date,
                       'post_id': post_id, 'comments_id': comment.id, 'coments_like': comment.comments_likes.count()}
        return JsonResponse(answer_dict)
    else:
        return JsonResponse({'text': '', })
