from django.db import models
from drink import Ingredient, Drink
from django.contrib.auth import User
# Create your models here.


class UserIngredient(models.Model):

    userID = models.ForeignKey(User)
    ingredientID = models.ForeignKey(Ingredient)
    amount = models.IntegerField()


class UserFavorite(models.Model):

    userID = models.ForeignKey(User)
    drinkID = models.ForeignKey(Drink)
