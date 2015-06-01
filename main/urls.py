from django.conf.urls import url, patterns
from main import views
from django.conf.urls.static import static
from Placeholder import settings


urlpatterns = patterns('',
    url(r'^$', views.home, name='homepage'),
    url(r'^default/$', views.dimension, name='default'),
    url(r'^(?P<values>[d\w]+)/$', views.dimension, name='dimension'),
    # the sequence matters. with_text should come first before with_color
    url(r'^(?P<values>[d\w]+)/t/(?P<text>[\-\w ]+)/$', views.dimension, name='with_text'),
    url(r'^(?P<values>[d\w]+)/c/(?P<color>[d\w].+)/$', views.dimension, name='with_color'),
    # throws error, look into it.
    # url(r'^(?P<values>[d\w]+)/(?P<color>[d\w].+)/(?P<text>[\-\w]+)/$', views.dimension, name='with_color'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
