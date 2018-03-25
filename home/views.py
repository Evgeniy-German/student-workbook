from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],)
            user.save()
            return HttpResponseRedirect("login")
    else:
        form = UserForm()
    return render(request, 'home/registration.html', {'form': form})


def main_page(request):
    return render(request, 'home/home.html')

