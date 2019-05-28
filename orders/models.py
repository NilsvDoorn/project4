from django.db import models

# Create your models here.
class Orders(models.Model):
    username = models.CharField(max_length=64)
    product = models.CharField(max_length=30)
    topping1 = models.CharField(max_length=16, null=True, blank=True)
    topping2 = models.CharField(max_length=16, null=True, blank=True)
    topping3 = models.CharField(max_length=16, null=True, blank=True)
    extra_kaas = models.BooleanField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        if self.topping3:
            return f"{self.product} with {self.topping1}, {self.topping2} and {self.topping3}"
        elif self.topping2:
            return f"{self.product} with {self.topping1} and {self.topping2}"
        elif self.topping1:
            return f"{self.product} with {self.topping1}"
        elif self.extra_kaas:
            return f"{self.product} with extra cheese"
        else:
            return f"{self.product}"

class Products(models.Model):
    categorie = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    toppings = models.IntegerField(null=True, blank=True)
    price_small = models.FloatField(null=True, blank=True)
    price_large = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.categorie}, {self.product}, {self.price_small}, {self.price_large}"

class All_orders(models.Model):
    username = models.CharField(max_length=64)
    product = models.CharField(max_length=40)
    price = models.FloatField()

    def __str__(self):
        return f"{self.product}"
