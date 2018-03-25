import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'e5#&f)(3!mb%rv-#1a(*izhx)1)6c3hkyvf2c#gs*pt7i)!q=t'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'home',
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #my apps
    'Markdown',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'CourseProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'CourseProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'course_project',
        'USER': 'root',
        'PASSWORD': 'root',
        'OPTIONS': {'charset': 'utf8'},
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/'

LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = 'login'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

SOCIAL_AUTH_TWITTER_KEY = 'jTmOhVwEvy6qOD561v9TpTMh2'
SOCIAL_AUTH_TWITTER_SECRET = '5bcBsdBLEUK2L3uxjfu1TVUa7yKHxrnZEc4DpE8AsHKa1gB6s5'

SOCIAL_AUTH_FACEBOOK_KEY = '196375687790418'
SOCIAL_AUTH_FACEBOOK_SECRET = '47aa9c96b6b2a9ed1d562c4fd13d189c'

SOCIAL_AUTH_VK_OAUTH2_KEY = '6402890'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'sZdkFiTsSW1yU3cahCwe'

SOCIAL_AUTH_GITHUB_KEY = '208ed54b538dcb12e384'
SOCIAL_AUTH_GITHUB_SECRET = 'bcef8734550b298a72fb86e349f8b44294597b22'
