from django.db import models
from utils.db.models import BaseModel
from authservice.models import User
# Create your models here.

class Account(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)



class Address(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    flat = models.CharField(max_length=50)
    street_address = models.CharField(max_length=255)
    near_by_landmark = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    is_default = models.BooleanField(default=False)

