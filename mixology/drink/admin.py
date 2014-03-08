from django.contrib import admin
from drink.models import Ingredient, Drink, Tag
# Register your models here.


admin.site.register(Drink)
admin.site.register(Ingredient)
admin.site.register(Tag)