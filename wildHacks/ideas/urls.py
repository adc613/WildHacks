from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
        url(r'^idea/(?P<pk>\d+)/$', IdeaDetailView.as_view(), name='detail'),
        url(r'^idea_list/$', IdeaListView.as_view(), name='list'),
        url(r'^create/$', IdeaCreationView.as_view(), name='create')
        )
