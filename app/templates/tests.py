from django.test import TestCase
from .models import ExampleModel

class ExampleModelTest(TestCase):
    def test_example_model_creation(self):
        model = ExampleModel.objects.create(name="Test Model")
        self.assertEqual(model.name, "Test Model")
