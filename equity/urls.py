"""equity URL Configuration

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
from django.conf import settings
from django.contrib import admin
from stocklist.views import picks, refresh
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Home, name='index'),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^mylist/$', views.Mylist),
    url(r'^get_tickr/$', views.get_tickr),
    url(r'^add_stock/$', views.add_stock),
    url(r'^delete_stock/$', views.delete_stock),
    url(r'^stocks/$', include('stocklist.urls')),
    url(r'^picks/$', picks),
    url(r'^stockrefresh/$', refresh),
]
