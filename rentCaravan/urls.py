"""rentCaravan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include

from application.views import answers_list, orders_list, products_list, profiles_list, questions_list, index, special, user_logout, register, user_login, profile_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('answers', answers_list),
    path('orders', orders_list),
    path('products', products_list),
    path('profiles', profiles_list),
    path('questions', questions_list),
    url(r'^$', index, name='index'),
    url(r'^special/', special, name='special'),
    url(r'^application/', include('application.urls')),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('profile', profile_page),

]
