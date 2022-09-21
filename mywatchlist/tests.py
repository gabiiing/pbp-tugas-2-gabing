from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_my_watch_list, show_xml, show_json


class Test_Data_Delivery_URLs(SimpleTestCase):
    def test_data_delivery_HTML(self):
        url = reverse('mywatchlist:show_my_watch_list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, show_my_watch_list)
    def test_data_delivery_JSON(self):
        url = reverse('mywatchlist:show_json')
        print(resolve(url))
        self.assertEqual(resolve(url).func, show_json)
    def test_data_delivery_XML(self):
        url = reverse('mywatchlist:show_xml')
        print(resolve(url))
        self.assertEqual(resolve(url).func, show_xml)
    

