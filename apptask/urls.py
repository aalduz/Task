from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.app),
    url(r'^summary/$', views.summary),
    url(r'^summary-average/$', views.summary_average),
    url(r'^site/(?P<pk>[0-9]+)/$', views.site_detail),    
)