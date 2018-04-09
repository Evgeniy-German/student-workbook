from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from Post.forms import PostForm
from Post.models import Post, Comments
# Create your views here.
from Tags.models import Tag


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comments.objects.filter(comments_post_id=post_id)
    form = PostForm(instance=post)
    d = {'post': post,
         'comments': comments,
         'form': form,
         }
    try:
        d['theme'] = request.session['theme']
    except KeyError:
        pass
    return render(request, 'home/post.html', d)


def addlike(request, post_id, comment_id):
    user = request.user
    comment = get_object_or_404(Comments, id=comment_id)
    if user.is_authenticated:
        if user in comment.comments_likes.all():
            comment.comments_likes.remove(user)
        else:
            comment.comments_likes.add(user)
        comment.save()
    return HttpResponseRedirect('/' + str(post_id))


def my_profile(request):
    if request.method == 'POST':
        return delete_post(request)
    elif request.user.is_authenticated:
        posts = Post.objects.filter(post_author=request.user)
        d = {'posts': reversed(posts), }
        try:
            d['theme'] = request.session['theme']
        except KeyError:
            pass
        return render(request, 'home/MyProfile.html', d)
    else:
        return HttpResponseRedirect('/')


def create_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.post_speciality_number = form.cleaned_data['post_speciality_number']
            post.post_short_description = form.cleaned_data['post_short_description']
            post.post_text = form.cleaned_data['post_text']
            post.post_title = form.cleaned_data['post_title']
            post.post_author = request.user
            post.save()
            tags = form.cleaned_data['tags']
            for tag in tags:
                post.tag_set.add(tag)
                tag.post_set.add(post)
            if request.POST['tag'] != '':
                new_tag, _ = Tag.objects.get_or_create(tag_name=request.POST['tag'])
                new_tag.save()
                post.tag_set.add(new_tag)
                new_tag.post_set.add(post)
            post.save()
            return HttpResponseRedirect('/MyProfile/')
    else:
        form = PostForm()
    d = {'form': form, }
    try:
        d['theme'] = request.session['theme']
    except KeyError:
        pass
    return render(request, 'home/EditPost.html', d)


def edit_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST)
    if request.method == 'POST' and user.is_authenticated and post.post_author == user and form.is_valid():
        post.post_speciality_number = form.cleaned_data['post_speciality_number']
        post.post_short_description = form.cleaned_data['post_short_description']
        post.post_text = form.cleaned_data['post_text']
        post.post_title = form.cleaned_data['post_title']
        tags = form.cleaned_data['tags']
        for tag in tags:
            post.tag_set.add(tag)
            tag.post_set.add(post)
        if request.POST['tag'] != '':
            new_tag, _ = Tag.objects.get_or_create(tag_name=request.POST['tag'])
            new_tag.save()
            post.tag_set.add(new_tag)
            new_tag.post_set.add(post)
        form = PostForm(instance=post)
        post.save()
        return render(request, 'home/EditPost.html',
                      {'form': form, 'good_news': 'True', })
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
                       'post_id': post_id, 'comments_id': comment.id, 'comments_likes': comment.comments_likes.count()}
        return JsonResponse(answer_dict)
    elif Comments.objects.filter(comments_post_id=post_id).count() != count:
        comment = Comments.objects.filter(comments_post_id=post_id)
        comment = comment[count:count + 1]
        comment = comment[0]
        user = comment.comments_author
        answer_dict = {'text': comment.comments_text, 'author': user.username, 'date': comment.comments_date,
                       'post_id': post_id, 'comments_id': comment.id, 'comments_likes': comment.comments_likes.count()}
        return JsonResponse(answer_dict)
    else:
        return JsonResponse({'text': '', })


def sort(request):
    if request.method == 'POST':
        if request.POST['sort'] == 'date':
            posts = Post.objects.all().order_by('post_date').filter(post_author=request.user)
        else:
            posts = Post.objects.filter(ratings__isnull=False).order_by(
                '-ratings__average').filter(post_author=request.user)
        try:
            if request.POST['inverse'] == 'true':
                posts = reversed(posts)
        except MultiValueDictKeyError:
            pass
        finally:
            return render(request, 'home/MyProfile.html', {'posts': posts})
    else:
        return render(request, 'home/MyProfile.html')
