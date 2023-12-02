from django.test import TestCase
from .models import Champ

class MyTestCase(TestCase):
    def test_model_name(self):
        champ = Champ.objects.create(name="bsuchjx", type="egs", description="deascgarev")
        self.assertEqual(champ.name, "bsuchjx")

    def test_model_type(self):
        champ = Champ.objects.create(name="bsuchjx", type="egs", description="deascgarev")
        self.assertEqual(champ.type, "egs")

    def test_model_description(self):
        champ = Champ.objects.create(name="bsuchjx", type="egs", description="deascgarev")
        self.assertEqual(champ.description, "deascgarev")

    def test_model_more(self):
        champ = Champ.objects.create(name="tcgjh", type="egs", description="tcgjh")
        self.assertEqual(champ.description, "tcgjh")
