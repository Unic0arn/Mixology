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
    image = models.CharField(max_length=255)
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()


class Recipe(models.Model):

    drinkID = models.ForeignKey('Drink')
    ingredientID = models.ForeignKey('Ingredient')


class Tag(models.Model):
    drinkID = models.ForeignKey('Drink')
    name = models.CharField(max_length=255)