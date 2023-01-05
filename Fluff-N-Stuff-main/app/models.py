from django.db import models

# Create your models here.

class Product(models.Model):
    customer_id= models.CharField(max_length=200, null=True, blank=True)
    customer_name= models.CharField(max_length=200, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_size = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.customer_name

