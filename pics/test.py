from django.test import TestCase
from .models import Image,Category,Location


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category_name = Category(category_name='FOOD')
        self.category_name.save()

    def tearDown(self):
        category_name.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category_name, Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category_name.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.image_location = Location(location_name='UK')
        self.image_location.save()

        self.image_category = Category(category_name='food')
        self.image_category.save()
#
        self.image_zoo = Image(image_name='image_zoo', description='nairobi is the biggest city in africa',image_location=self.image_location, image_category=self.image_category)
        self.image_zoo.save_image()

        
    def test_instance(self):
        self.assertTrue(isinstance(self.image_zoo, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image_zoo.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_zoo.save_image()
        self.image_zoo.delete_image()       
        self.assertTrue(len(images) == 0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='uk')
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