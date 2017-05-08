from django.conf.urls import url

from catalog.views import category, product, product_list

urlpatterns = [
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', category, name='category'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', product, name='product')

]
