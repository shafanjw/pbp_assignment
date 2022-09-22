from urllib import response
from django.test import TestCase
from django.test import Client

# Buat testcase untuk ketiga url
class TestUrl(TestCase):
    def test_html_exists(self):
        response= Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_xml_exists(self):
        response= Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
    
    def test_json_exists(self):
        response =Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)