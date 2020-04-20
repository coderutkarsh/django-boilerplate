from django.db import models
from django.core import serializers
from django.forms.models import model_to_dict
# Create your models here.


class Product (models.Model):
    #these are the specific fields defined in documentation : https://docs.djangoproject.com/en/3.0/ref/models/fields/#textfield
    name =  models.CharField(max_length=200)
    desc = models.TextField()
    price = models.IntegerField()

    # def __str__(self):
    #     return self.name
    def __repr__(self):
        """Return string representation of a set.

        This looks like 'Set([<list of elements>])'.
        """
        return self.name


    # def __init__(self, name, desc, price):
    #     print("constructor invoked",name,desc,price)
    #     self.name = name
    #     self.desc = desc
    #     self.price = price

    def create_product(self, name,desc,price):
        product = self.create(name=name,desc=desc,price=price)
        # do something with the book
        return product

    def sampleFunc(self):
        print("Sample function called")



