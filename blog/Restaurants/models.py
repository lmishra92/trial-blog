from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RestaurantCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Restaurants(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=250)
    category = models.ManyToManyField(RestaurantCategory)
    slug = models.SlugField(max_length=250)
    logo = models.ImageField()
    delivery_available = models.BooleanField()
    delivery_details = models.CharField(max_length=250, default="This restaurant doesn't deliver")
    signature_dish = models.CharField(max_length = 250)
    address = models.URLField(max_length=500)
    website = models.URLField(max_length=200)
    fb_page = models.URLField(max_length=200)

    def __str__(self):
        return self.name

