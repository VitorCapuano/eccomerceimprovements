
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contato/$', contact_form, name='contact'),
    url(r'^entrar/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', admin.site.urls)

]
