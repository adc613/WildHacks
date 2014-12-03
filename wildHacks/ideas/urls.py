from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
        url(r'^idea/(?P<pk>\d+)/$', IdeaDetailView.as_view(), name='detail'),
        url(r'^upvote/(?P<pk>\d+)/$', like_view, name='like'),
        url(r'^downvote/(?P<pk>\d+)/$', dislike_view, name='dislike'),
        url(r'^idea_list/$', IdeaListView.as_view(), name='list'),
        url(r'^create/$', IdeaCreationView.as_view(), name='create'),
        url(r'^search/$', SearchView.as_view(), name='search'),
        )
