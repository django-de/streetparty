from django.conf.urls import patterns, include, url

from .views import StrassenFestList

urlpatterns = patterns('',
    url(r'^$', StrassenFestList.as_view(), name='feste'),
)
