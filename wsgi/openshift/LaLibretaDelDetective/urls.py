from django.conf.urls import patterns, url
import LaLibretaDelDetective 

urlpatterns = patterns('',
    url(r'^$', LaLibretaDelDetective.views.index, name='index')
)