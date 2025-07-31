from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=15)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name='product')
    
    def __str__(self):
        return self.name