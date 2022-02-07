from unicodedata import category
from django.db import models
from utils.base_model import BaseModel

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=256)
    country_of_origin = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    variant_id = models.CharField(max_length=12, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    stock_threshold = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

class ProductImage(models.Model):
    image_id = models.CharField(max_length=100)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
