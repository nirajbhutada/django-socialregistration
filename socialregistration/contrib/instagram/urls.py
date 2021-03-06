from django.conf import settings
from socialregistration.compat.urls import *
from socialregistration.contrib.instagram.views import InstagramRedirect, \
    InstagramCallback, InstagramSetup
 
urlpatterns = patterns('',
    url('^redirect/$', InstagramRedirect.as_view(), name='redirect'),
    url('^callback/$', InstagramCallback.as_view(), name='callback'),
    url('^setup/$', InstagramSetup.as_view(), name='setup'),
)
