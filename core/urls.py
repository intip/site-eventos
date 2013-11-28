#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from .views import EventsContactFormView

urlpatterns = patterns(
    'core.views',
    url(r'^$', EventsContactFormView.as_view(), name='homepage'),
    url(r'^(?P<page>\w+)/$', 'pages', name='pages')
)
