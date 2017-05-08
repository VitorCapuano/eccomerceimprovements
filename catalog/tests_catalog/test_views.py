from django.test import TestCase, Client

from catalog.models import Category, Product
from model_mommy import mommy
from django.core.urlresolvers import reverse


class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.products = mommy.make('catalog.Product', _quantity=10)
        self.client = Client()

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/products_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('products' in response.context)
        product_list = response.context['products']
        self.assertEquals(product_list.count(), 10)


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(self.product.get_absolute_url(),
                reverse('catalog:product', kwargs={'slug': 'produto'})
            )