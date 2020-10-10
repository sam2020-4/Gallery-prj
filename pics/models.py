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

class Image(models.Model):    
    image_name = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=10, default='admin')
    image = models.ImageField(upload_to = 'images/')
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)    

    def __str__(self):
        return self.image_name

