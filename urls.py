from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from deco.front.models import *
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'deco.front.views.home', name='home'),
    # url(r'^deco/', include('deco.foo.urls')),
    (r'^(?P<item>\w+)/$', 'deco.front.views.item_page'),
    # url(r'^deco/', include('deco.foo.urls')),
)
