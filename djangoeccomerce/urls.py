
from django.conf.urls import url, include
from django.contrib import admin

from core.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contato/$', contact_form, name='contact'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls)

]
