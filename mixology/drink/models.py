from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255,blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    ingredients = models.ForeignKey('Ingredient',)

class Tag(models.Model):
    drinkID = models.ForeignKey('Drink')
    name = models.CharField(max_length=255)