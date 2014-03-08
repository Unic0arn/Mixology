from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Drink

# Create your views here.


def main(request):
    drink = Drink(name='Mojito', description='Yum!')
    drink2 = Drink(name='Cuba Libre', description='Yuck!')
    # WHYY DOESNT IT WOOORK
    args = {'drinks': [drink, drink2]}
    return render_to_response("mixology/index.html", args, RequestContext(request))


