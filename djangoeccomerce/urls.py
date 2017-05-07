
from django.conf.urls import url
from django.contrib import admin

from core.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contato/$', contact, name='contact'),
    url(r'^produto/$', product, name='product'),
    url(r'^produtos/$', product_list, name='product_list'),
    url(r'^admin/', admin.site.urls)

]
