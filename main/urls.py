from django.conf.urls import url, patterns
from main import views
from django.conf.urls.static import static
from Placeholder import settings

urlpatterns = patterns('',
    url(r'^$', views.home, name='homepage'),
    url(r'^default/$', views.dimension, name='default'),
    url(r'^(?P<values>[d\w]+)/$', views.dimension, name='dimension'),
    url(r'^(?P<values>[d\w]+)/as/(?P<color>[d\w].+)/$', views.dimension),
    #url(r'^(?P<values>[d\w]+)/as/(?P<color>[d\w].+)/(?P<alpha>[\w]+)/$', views.dimension), 
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
