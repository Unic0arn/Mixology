from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)
    upvotes = models.IntegerField(default=1)
    downvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    @property
    def upvoteperc(self):
        ups = self.upvotes
        downs = self.downvotes
        upperc = 100
        if ups + downs != 0:
            upperc = int((ups / float(ups + downs)) * 100)
        return upperc

    @property
    def downvoteperc(self):
        ups = self.upvoteperc
        return 100 - ups


class Recipe(models.Model):
    drink = models.ForeignKey('Drink')
    ingredient = models.ForeignKey('Ingredient')
    amount = models.IntegerField(default=1)
    note = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return  str(self.amount) + " " + self.ingredient.unit + " of " + self.ingredient.name + " in " + self.drink.name


class Tag(models.Model):
    drink = models.ForeignKey('Drink')
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name