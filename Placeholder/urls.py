from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^help/', include('django.contrib.flatpages.urls')),
)
