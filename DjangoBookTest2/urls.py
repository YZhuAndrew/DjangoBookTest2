from django.conf.urls import patterns, include, url
from django.contrib import admin
from DjangoBookTest2.views import current_datetime
from DjangoBookTest2.views import display_meta
from books.views import search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoBookTest2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url(r'^meta/$', display_meta),
    url(r'^search/$', search),
)
