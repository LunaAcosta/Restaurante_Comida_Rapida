from django.test import SimpleTestCase 
from django.urls import reverse,  resolve 
from inicio.views import * 

class Testurls(SimpleTestCase):

    def test_url(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func,acercade)
        