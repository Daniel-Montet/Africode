"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^api/v1/courses', include('courses.api_urls', namespace='courses_api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^suggest/$', views.suggestion_view, name='suggestion'),
    url(r'^$', views.home_page, name='home'),
    url(r'^about-us$', views.aboutus_view, name='about_us'),
    url(r'^blog$', views.blog_view, name='blog'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()