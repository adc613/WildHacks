from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('',
        url(r'^idea/(?P<pk>\d+)/$', IdeaDetailView.as_view(), name='detail'),
        url(r'^idea_list/$', IdeaListView.as_view(), name='list'),
        url(r'^create/$', IdeaCreationView.as_view(), name='create'),

        # Generic view to vote on Link objects
    	(r'^links/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$',
        vote_on_object, dict(model=Link, template_object_name='link',
            template_name='kb/link_confirm_vote.html',
            allow_xmlhttprequest=True)),
        )
