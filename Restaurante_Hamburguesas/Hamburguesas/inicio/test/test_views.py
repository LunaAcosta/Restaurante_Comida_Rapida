from django.test import TestCase, Client
from django.urls import reverse
from inicio.views import * 


class TestViews(TestCase):

    def test_view(self):
        client = Client()

        response= client.get(reverse('inico'))
        self.assertEquals(response.status_code,200)
        self.assertTempleUsed(response, 'index.html')
        