from django.test import TestCase
from .models import Location, Image, Category

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Nairobi')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location_name = 'kenya'
        self.location.update_location(self.location.id, new_location_name)
        updated_location = Location.objects.filter(location_name='kenya')
        self.assertTrue(len(updated_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='People')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
