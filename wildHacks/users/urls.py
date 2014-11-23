from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wildHacks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', LoginView.as_view(), name='login'),
     url(r'^sign_up/$', SignUpView.as_view(), name='sign_up'),
    url(r'^logout/$', logout_view, name='logout')
)
