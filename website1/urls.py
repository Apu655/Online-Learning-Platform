"""website1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calc.views import home_view,navbar_view, search_view,course_view
from user.views import SignUp,signIn,signOut, successfulSignUp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('navbar/',navbar_view,name='navbar'),
    path('SignUp/',SignUp,name='SignUp'),
    path('signIn/',signIn, name = 'signIn'),
    path('signOut/',signOut, name='signOut'),
    path('search/',search_view, name = "search"),
    path('course/',course_view,name='course'),
    path('signUpSuccessful/',successfulSignUp,name="successfulSignUp"),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)