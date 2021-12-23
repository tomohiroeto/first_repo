from django.db import models
from mamazon.models import Product
from django.conf import settings
from mamazon.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Product = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.ImageField(auto_now=True)

    def __str__(self):
        return self.name
