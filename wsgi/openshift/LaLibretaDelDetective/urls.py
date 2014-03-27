from LaLibretaDelDetective import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^libreta_create$', views.libreta_create, name='libreta_create'),
    url(r'^libreta_save$', views.libreta_save, name='libreta_save'),
    url(r'^libreta$', views.libreta, name='libreta'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login$', views.login, name='login'),
    url(r'^admin$', views.admin, name='admin'),
)