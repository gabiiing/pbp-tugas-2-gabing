from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_html, show_xml, show_json


class Test_Data_Delivery_URLs(TestCase):
    def test_data_delivery_HTML(self):
        url = reverse('mywatchlist:show_html')
        print(resolve(url))
        self.assertEqual(resolve(url).func, show_html)
    def test_data_delivery_JSON(self):
        url = reverse('mywatchlist:show_json')
        print(resolve(url))
        self.assertEqual(resolve(url).func, show_json)
    def test_data_delivery_XML(self):
        url = reverse('mywatchlist:show_xml')
        print(resolve(url))
        self.assertEqual(resolve(url).func, show_xml)
    

