from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main_page),
    path(r'<int:post_id>', views.post),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path(r'activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('summernote/', include('django_summernote.urls')),
]
