from django.conf.urls import patterns, url
from LaLibretaDelDetective import views 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^libreta_create$', views.libreta_create, name='libreta_create'),
    url(r'^libreta_save$', views.libreta_save, name='libreta_save'),
    url(r'^libreta$', views.libreta, name='libreta'),
    url(r'^admin$', views.admin, name='admin'),
)