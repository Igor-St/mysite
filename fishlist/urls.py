# -*- coding: utf8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^articles/all/$', views.articles, name='articles'),
    #url(r'^articles/get/(?P<article_id>[0-9]+)/$', views.article, name='article'),
    #url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', views.addlike, name='addlike'),
    url(r'^(?P<id>[0-9]+)/addcomment/$', views.addcomment, name='addcomment'),
    #url(r'^page/(\d+)/$', views.articles, name='articles'),
    url(r'^$', views.index, name='index'),
    #url(r'^page/(\d+)/$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.fish, name='fish'),
    url(r'^add_fish/$', views.add_fish, name='add_fish'),
    #url(r'^edit_fish/(?P<id>[0-9]+)/$', views.edit_fish, name='edit_fish'),
    url(r'^(?P<id>[0-9]+)/edit_fish/$', views.edit_fish, name='edit_fish'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    #url(r'^logout/$', views.user_logout, name='logout'),
]