from django.db import models

# Create your models here.
# db relashionships
class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
    def __str__(self):
        return self.category_name

