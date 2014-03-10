from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Drink, Ingredient, Recipe, Tag
from login.models import UserFavorite
from django.core.context_processors import csrf

# Create your views here.


def main(request):
    args = {}
    args['drinks'] = Drink.objects.all()
    args.update(csrf(request))
    return render_to_response("mixology/index.html", args, RequestContext(request))

def favorites(request):
    user = request.user
    favorites = user.userfavorite_set.all().prefetch_related()
    args = {}
    args['favorites'] = favorites

    args.update(csrf(request))
    return render_to_response("mixology/favorites.html",args, RequestContext(request))

def remove_favorite(request, drink_id):
    print "lol2"
    user = request.user
    print user
    drink = Drink.objects.get(pk=drink_id)
    print drink
    fav, created = UserFavorite.objects.get_or_create(drinkID=drink,userID=user)
    print fav
    fav.delete()
    print "deleted"
    return HttpResponse('')

def add_favorite(request, drink_id):
    print "lol"
    user = request.user
    print user
    drink = Drink.objects.get(pk=drink_id)
    print drink
    fav, created = UserFavorite.objects.get_or_create(drinkID=drink,userID=user)
    print fav
    return HttpResponse('')


def search_drinks(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    drinks = set(Drink.objects.filter(name__icontains=search_text))

    tag_drinks = set(Tag.objects.filter(name__iexact=search_text).prefetch_related('drink'))
    print tag_drinks
    for tag in tag_drinks:
        print tag.drink
        drinks.add(tag.drink)

#    drinks = drinks.order_by('upvoteperc')
    return render_to_response("drink/ajax_search.html", {'drinks': list(drinks)}, RequestContext(request))


def add_tag(request, drink_id):
    drink = Drink.objects.get(pk=drink_id)
    print drink
    tag, created = Tag.objects.get_or_create(name=request.POST['tag'], drink=drink)
    tag.save()
    print tag
    tags = drink.tag_set.all()
    print tags
    args = {}
    args.update(csrf(request))
    args['tags'] = tags
    return render_to_response("drink/tag_list.html", args, RequestContext(request))


def advanced_search(request):
    if request.method == "POST":
        cabinet = request.POST.getlist('ingredients')
        args = {}
        args.update(csrf(request))
        cabinet = map(int, cabinet)
        print cabinet
        ingredientIds = set(cabinet)
        print ingredientIds
        drinkids = set(Drink.objects.values_list('id', flat=True))
        #ingredients = Ingredient.objects.filter(id__in=cabinet)
        print drinkids
        drinkList = set()
        for d in drinkids:
            print d

            di = Recipe.objects.filter(drink__id=d)
            print di
            diid = set(di.values_list('ingredient__id', flat=True))
            print diid
            if diid.issubset(ingredientIds):
                print "Woho"
                drinkList.add(d)
            else:
                print "Removing"

        print drinkList

        '''
        for i in cabinet:
            ing = Ingredient.objects.get(id=i)
            reclist = ing.recipe_set.all()
            tempdrinkids = set()

            print ing
            for r in reclist:
                print r.drink
                tempdrinkids.add(r.drink.id)
            print tempdrinkids
            if len(drinkids) == 0:
                drinkids = tempdrinkids
            else:
                drinkids = drinkids & tempdrinkids
            print drinkids
        '''
        args['drinks'] = Drink.objects.filter(pk__in=drinkList)  # .order_by('upvoteperc')
        args['ingredients'] = Ingredient.objects.all()

        return render_to_response("drink/ajax_search.html", args, RequestContext(request))

    else:
        args = {}
        args['ingredients'] = Ingredient.objects.all()
        args['drinks'] = Drink.objects.all()  # order_by('upvoteperc')
        args.update(csrf(request))
        return render_to_response("drink/search.html", args)


def drink_view(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    recipe = drink.recipe_set.all()
    tags = drink.tag_set.all()

    args = {}
    args['tags'] = tags
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
    print "Upvotes: " + str(drink.upvotes) + " \nDownVotes: " + str(drink.downvotes)
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