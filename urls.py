from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'developer.dev.views.home', name='home'),
    url(r'^modules/$', 'developer.dev.views.modules', name='modules'),
    url(r'^submodules/$', 'developer.dev.views.submodules', name='submodules'),
    url(r'^ideas/$', 'developer.ideas.views.idea', name='idea'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)





