from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Drink
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
    print search_text
    drinks2 = Drink.objects.filter(name__contains=search_text)
    print drinks2
    print "searching"
    args = {}
    args['drinks'] = drinks2
    return render_to_response("drink/ajax_search.html", {'drinks': drinks2})



def init(request):
    Drink(name='Mojito', description='Yum!').save()
    Drink(name='Cuba Libre', description='Yuck!').save()
    return main(request)