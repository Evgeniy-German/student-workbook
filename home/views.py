from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string

from Post.models import Post
from .forms import SignupForm
from .tokens import account_activation_token
from Tags.models import Tag


def main_page(request):
    return render(request, 'home/home.html', {'posts': reversed(Post.objects.all().order_by('post_date_update')),
                                              'sorted_posts': Post.objects.filter(ratings__isnull=False).order_by(
                                                  '-ratings__average'),
                                              'tags': Tag.objects.all()})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render_to_response('../templates/registration/registration_response.html',
                                      {'complete': 'Please confirm your email address to complete the registration',
                                       'error': 'None'})
    else:
        form = SignupForm()
    return render(request, '../templates/registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = uidb64
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponseRedirect('/login')
    else:
        return render_to_response('../templates/registration/registration_response.html',
                                  {'error': 'Activation link is invalid!', 'complete': 'None'})


def math_theme(request):
    user = request.user
    if user.is_authenticated:
        request.session['theme'] = 'math'
        return render(request, 'home/home.html', {'posts': reversed(Post.objects.all().order_by('post_date_update')),
                                                  'sorted_posts': Post.objects.filter(ratings__isnull=False).order_by(
                                                      '-ratings__average'),
                                                  'tags': Tag.objects.all(), 'theme': 'math', })
    else:
        return main_page(request)


def humanitarian_theme(request):
    user = request.user
    if user.is_authenticated:
        request.session['theme'] = 'humanitarian'
        return render(request, 'home/home.html', {'posts': reversed(Post.objects.all().order_by('post_date_update')),
                                                  'sorted_posts': Post.objects.filter(ratings__isnull=False).order_by(
                                                      '-ratings__average'),
                                                  'tags': Tag.objects.all(), 'theme': 'humanitarian', })
    else:
        return main_page(request)
