from django.test import  TestCase, Client


class Test_Data_Delivery_URLs(TestCase):
    def test_data_delivery_HTML(self):
        res=Client().get('/mywatchlist/html/')
        self.assertEqual(res.status_code, 200)
    
    def test_data_delivery_XML(self):
        res=Client().get('/mywatchlist/xml/')
        self.assertEqual(res.status_code, 200)
    
    def test_data_delivery_JSON(self):
        res=Client().get('/mywatchlist/json/')
        self.assertEqual(res.status_code, 200)