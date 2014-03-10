from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
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
    drinks2 = Drink.objects.filter(name__icontains=search_text)

    return render_to_response("drink/ajax_search.html", {'drinks': drinks2})


def advanced_search(request):
    if request.method == "POST":
        #cabinet = request.POST.getlist('ingredients')
        args = {}
        args.update(csrf(request))

        #ingredients = Ingredient.objects.filter(id__in=cabinet)

        args['drinks'] = Drink.objects.all()
        args['ingredients'] = Ingredient.objects.all()

        return render_to_response("drink/search.html", args, RequestContext(request))

    else:
        args = {}
        args['ingredients'] = Ingredient.objects.all()
        args.update(csrf(request))
        return render_to_response("drink/search.html", args)


def drink_view(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    recipe = drink.recipe_set.all()

    args = {}
    args['drink'] = drink
    args['ingredients'] = recipe

    return render_to_response("drink/drink.html", args, RequestContext(request))


def vote(request, drink_id):
    oldvote = int(request.POST['oldvote'])
    newvote = int(request.POST['newvote'])
    drink = Drink.objects.get(id=drink_id)

    if oldvote == 0:
        if newvote == 1:
            #single upvote
            drink.upvotes += 1
        elif newvote == -1:
            #single downvote
            drink.downvotes += 1
    elif oldvote == 1:
        if newvote == 0:
            #remove upvote
            drink.upvotes -= 1
        elif newvote == -1:
            #remove upvote and add downvote
            drink.upvotes -= 1
            drink.downvotes += 1
    elif oldvote == -1:
        if newvote == 0:
            #remove downvote
            drink.downvotes -= 1
        elif newvote == 1:
            #remove downvote and add upvote
            drink.downvotes -= 1
            drink.upvotes += 1
    drink.save()
    return HttpResponse('')


def init(request):
    drink1 = Drink(name='Mojito', description='Yum!', image='mojito.jpg')
    drink1.save()
    drink2 = Drink(name='Cuba Libre', description='Yuck!', image='cuba.jpg')
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