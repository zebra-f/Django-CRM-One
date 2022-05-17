from django.db import models


# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):

    CATEGORIES = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )

    name = models.CharField(max_length=128, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=128, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=256, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )

    # customer 
    # product 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=16, null=True, choices=STATUS)