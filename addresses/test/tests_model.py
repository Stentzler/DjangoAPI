from django.test import TestCase
from addresses.models import Address
from django.forms.models import model_to_dict


class AddressesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_address={
            "zipcode":"44090736",
            "district": "Salvador",
            "state":"Bahia",
            "street": "rua g",
            "number": "53"
        }

        cls.addressTest = Address.objects.create(**cls.test_address)

    def test_key_address(self):   
        dic = model_to_dict(self.addressTest)
        self.assertEqual(self.test_address.keys(), dic.keys())




    

