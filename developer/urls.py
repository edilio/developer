from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.dev.views.home', name='home'),
    url(r'^modules/$', 'apps.dev.views.modules', name='modules'),
    url(r'^submodules/$', 'apps.dev.views.submodules', name='submodules'),
    url(r'^ideas/$', 'apps.ideas.views.ideas', name='ideas'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)





