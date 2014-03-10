# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from drink import views


urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^search/', views.search_drinks),
    url(r'^advancedsearch/', views.advanced_search),
    url(r'^init/', views.init),
    url(r'^favorites', views.favorites, name="favorites"),
    url(r'^(?P<drink_id>\d+)/vote/', views.vote),
    url(r'^(?P<drink_id>\d+)/addfav/', views.add_favorite),
    url(r'^(?P<drink_id>\d+)/removefav/', views.remove_favorite),
    url(r'^(?P<drink_id>\d+)/add-tag/', views.add_tag),
    url(r'^(?P<drink_id>\d+)/$', views.drink_view),
    )
