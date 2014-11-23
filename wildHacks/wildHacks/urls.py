from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^thanks/$', ThankYouView.as_view(), name='thanks'),

    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^ideas/', include('ideas.urls', namespace='ideas')),
    #url(r'^users/', include('users.urls'), namespace='users'),

    url(r'^admin/', include(admin.site.urls)),
)
