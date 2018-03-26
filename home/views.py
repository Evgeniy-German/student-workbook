from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render


def password_valid(request):
    post = request.POST
    if post['password1'] == post['password2'] and len(post['password1']) >= 8:
        return True
    else:
        return False


def email_valid(request):
    post = request.POST
    s = post['email'][:2]
    if '@' in post['email'] and '.' in post['email'] and '.' not in s and '@' not in s and len(post['email']) > 6:
        return True
    else:
        return False


def is_valid(request):
    if email_valid(request) and password_valid(request):
        return True
    else:
        return False


def registration(request):
    if request.method == 'POST':
        if is_valid(request):
            user = User(email=request.POST['email'],
                        password=make_password(request.POST['password1']),
                        username=request.POST['username'])
            try:
                user.save()
            except IntegrityError:
                return render(request, 'home/registration.html', {'error': 'user_exists'})
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'home/registration.html', {'error': 'true'})
    return render(request, 'home/registration.html', )


def main_page(request):
    return render(request, 'home/home.html')
