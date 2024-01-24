from django.db import models

from user.models import OwnerProfile, EmployeeProfile


class Restaurant(models.Model):
    owner = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=200, blank=True)
    address = models.TextField(max_length=500, blank=True)
    hotline_number = models.CharField(max_length=15, blank=True)
    opening_hours = models.TextField(max_length=1000, blank=True, null=True)
    managers = models.ManyToManyField(EmployeeProfile, related_name="restaurant_managers", blank=True)

    def __str__(self) -> str:
        return self.restaurant_name
    

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"{self.restaurant.restaurant_name} - {self.name}"
    

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.item_name}-{self.menu.name}"