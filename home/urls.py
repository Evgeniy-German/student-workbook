from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include

from Post import views as post_view
from . import views

urlpatterns = [
    path('', views.main_page),
    path(r'<int:post_id>/', post_view.post),
    path(r'<int:post_id>/<int:comment_id>/addlike/', post_view.addlike),
    path('MyProfile/', post_view.my_profile),
    path(r'MyProfile/<int:post_id>/edit/', post_view.edit_post),
    path(r'MyProfile/create/', post_view.create_post),
    path(r'add_comment/', post_view.add_comment, name='add_comment'),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path(r'activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),

    path('summernote/', include('django_summernote.urls')),

    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
