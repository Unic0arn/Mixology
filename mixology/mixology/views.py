# -*- coding: utf-8 -*-
from django.shortcuts import render
from drink.models import Drink


def main(request):
    drinks = Drink.objects.all()
    return render(request, 'mixology/index.html', {'drinks': drinks})