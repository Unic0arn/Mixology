from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Drink, Ingredient, Recipe
from django.core.context_processors import csrf

# Create your views here.


def main(request):
    args = {}
    args['drinks'] = Drink.objects.all()
    args.update(csrf(request))
    return render_to_response("mixology/index.html", args, RequestContext(request))


def search_drinks(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    drinks2 = Drink.objects.filter(name__contains=search_text)
    args = {}
    args['drinks'] = drinks2
    return render_to_response("drink/ajax_search.html", {'drinks': drinks2})


def drink_view(request, drink_id):
    print "here"
    drink = Drink.objects.get(id=drink_id)
    recipe = drink.recipe_set.all()

    return render_to_response("drink/drink.html", {'drink': drink, 'ingredients': recipe})


def init(request):
    drink1 = Drink(name='Mojito', description='Yum!')
    drink1.save()
    drink2 = Drink(name='Cuba Libre', description='Yuck!')
    drink2.save()
    i1 = Ingredient(name='Juice', description='So svalk', unit='kg')
    i1.save()
    i2 = Ingredient(name='Vatten', description='Such wet', unit='doge')
    i2.save()
    i3 = Ingredient(name='Vindruvor', description='Many rund', unit='pi')
    i3.save()
    i4 = Ingredient(name='Milk', description='Very ko', unit='mil-k')
    i4.save()
    Recipe(drink=drink1, ingredient=i1, amount=20).save()
    Recipe(drink=drink1, ingredient=i2, amount=20).save()
    Recipe(drink=drink1, ingredient=i4, amount=20, note="smaskens!").save()
    Recipe(drink=drink2, ingredient=i2, amount=20).save()
    Recipe(drink=drink2, ingredient=i4, amount=20, note="katt").save()

    return main(request)