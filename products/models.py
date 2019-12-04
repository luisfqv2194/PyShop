from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

# If any change is made is better to delete all the migrations and start from scratch
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class Offer(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=400)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    initial_date = models.DateField(default=timezone.now)  # Allows to change the date later
    ending_date = models.DateField(default=timezone.now)
