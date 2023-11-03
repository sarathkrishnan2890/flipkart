from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField(default='', blank=True, null=True)
    image_url = models.CharField(max_length=3000, blank=True, default=False)
    available = models.BooleanField(default=False)





class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(products)
    total_price = models.DecimalField(max_digits=11, decimal_places=5)


class CartItems(models.Model):
    book = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.book.price * self.quantity
