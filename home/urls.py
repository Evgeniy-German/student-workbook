from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include

from Post import views as post_view
from . import views as home_view
from Tags import views as tags_view

urlpatterns = [
    path('', home_view.main_page),
    path(r'<int:post_id>/', post_view.post),
    path(r'<int:post_id>/<int:comment_id>/addlike/', post_view.addlike),
    path('MyProfile/', post_view.my_profile),
    path(r'MyProfile/<int:post_id>/edit/', post_view.edit_post),
    path(r'MyProfile/create/', post_view.create_post),
    path(r'add_comment/', post_view.add_comment, name='add_comment'),
    path(r'tag/<int:tag_value>/', tags_view.show_posts_by_teg, name='sort_by_tag'),
    path('sort/', post_view.sort, name='sort'),
    path('math_theme/', home_view.math_theme, name='math_theme'),
    path('humanitarian_theme/', home_view.humanitarian_theme, name='humanitarian_theme'),
    path('i18n/', include('django.conf.urls.i18n')),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', home_view.signup, name='signup'),
    path(r'activate/<str:uidb64>/<str:token>/', home_view.activate, name='activate'),

    path('summernote/', include('django_summernote.urls')),

    path(r'ratings/', include('star_ratings.urls', namespace='ratings')),

    path('search/', include('haystack.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
