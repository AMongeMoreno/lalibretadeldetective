from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^libreta/', 'views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homes/', 'views.home', name='home'), 
)
