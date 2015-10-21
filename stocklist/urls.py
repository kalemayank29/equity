from django.conf.urls import include,url
from django.contrib import admin
from . import views

urlpatterns = [
#s    url(r'^admin/$', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.picks, name='picks'),
    url(r'^$', views.refresh, name='refresh'),
    #url(r'^stocks/$', include('stocklist.urls')),
]
