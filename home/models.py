from django.db import models
from utils.db.models import BaseModel

# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.ManyToManyField('home.color', related_name='products',null=True, blank=True)
    brand = models.OneToOneField('home.brand', on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    category = models.OneToOneField('home.category', on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    frame_size = models.OneToOneField('home.framesize',on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    wheel_size = models.OneToOneField('home.wheelsize',on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey('home.discount', on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)

class Discount(models.Model):
    discount_in_rupees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_in_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} - {self.price}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class FrameSize(models.Model):
    frame_size = models.CharField(max_length=30)
    frame_size_in_inches = models.IntegerField(null=True, blank=True)

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

class WheelSize(models.Model):
    wheel_size = models.CharField(max_length=30)
    wheel_size_in_inches = models.IntegerField(null=True, blank=True)

class Color(models.Model):
    color = models.CharField(max_length=30)
    hex_code = models.CharField(max_length=10)
