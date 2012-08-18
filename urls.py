from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from deco.front.models import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'deco.front.views.home', name='home'),
    # url(r'^deco/', include('deco.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
