from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField()
    stock = models.IntegerField()

    def get_absolute_url(self):
        return f"{self.id}"
        # return reverse('products:product_detail', kwargs={"id":self.id})
