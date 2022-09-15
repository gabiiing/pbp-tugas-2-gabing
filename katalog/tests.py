from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.
class katalog_test(TestCase):
    def setUp(self):
        CatalogItem.objects.get(item_name="Iphone XR", item_price=4000000, item_stock=100,
                                   description="New Iphone", rating=5, item_url="https://www.tokopedia.com/spiritcellular-1/iphone-xr-64gb-second-e-x-inter-original-no-minus-fullset-kuning?extParam=ivf%3Dfalse&src=topads")

    def test_is_dummy_valid(self):
        iphone_XR = CatalogItem.objects.get(item_name="Iphone XR", item_price=4000000, item_stock=100,
                                      description="New Iphone", rating=5, item_url="https://www.tokopedia.com/spiritcellular-1/iphone-xr-64gb-second-e-x-inter-original-no-minus-fullset-kuning?extParam=ivf%3Dfalse&src=topads")
        self.assertEqual(iphone_XR.item_name, "Iphone XR")
        self.assertEqual(iphone_XR.item_price, 4000000)
        self.assertEqual(iphone_XR.item_stock, 100)
        self.assertEqual(iphone_XR.description, "New Iphone")
        self.assertEqual(iphone_XR.rating, 5)
        self.assertEqual(iphone_XR. item_url, "https://www.tokopedia.com/spiritcellular-1/iphone-xr-64gb-second-e-x-inter-original-no-minus-fullset-kuning?extParam=ivf%3Dfalse&src=topads")