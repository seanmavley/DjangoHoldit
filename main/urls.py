# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from main.views import PlaceholderView
from main import views

kwargs = {
    'width':      r'(?P<width>\d+)',
    'height':     r'(?P<height>\d+)',
    'format':     r'(?P<format>gif|jpe?g|png)',
    'background': r'(?P<background>.*?)',
    'color':      r'(?P<color>.*?)',
    'text':       r'(?P<text>.*?)',
}


urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage'),
    url(r'^{width}(?:x{height})?(?:\.{format})?(?:/{background}(?:/{color})?)?(?:&text={text})?$'.format(**kwargs), PlaceholderView.as_view(), name='placeholder'),
)
