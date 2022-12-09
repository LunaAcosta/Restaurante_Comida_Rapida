from django.test import TestCase
from inicio.models import * 

class TestModels(TestCase):

    def test_model(self):
        self.SuculsalTest = Sucursal.objects.create(
                nombre = "San Miguel",
                direccion = "Col san maria",
                telefono =  "78449594"
        )

