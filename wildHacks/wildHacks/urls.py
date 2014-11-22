from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wildHacks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$/', HomePageView.as_view, name='home'),

    url(r'^users/', include(users.urls), namespace)
    url(r'^ideas/', include('ideas.urls'), namespace='ideas'),
    #url(r'^users/', include('users.urls'), namespace='users'),

    url(r'^admin/', include(admin.site.urls)),
)
