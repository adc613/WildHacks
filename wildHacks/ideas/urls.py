from django.contrib.urls import patterns, include, url

from .views import *

urlpatterns = url('',
        url(r'^idea/(?<pk>)/$', IdeaDetailView.as_view(), name='idea_detail'),
        url(r'^idea_list/$', IdeaListView,as_view(), name='idea_list'),
        )
