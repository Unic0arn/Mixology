from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    drink = models.ForeignKey('Drink')
    ingredient = models.ForeignKey('Ingredient')
    amount = models.IntegerField(default=1)


class Tag(models.Model):
    drinkID = models.ForeignKey('Drink')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name