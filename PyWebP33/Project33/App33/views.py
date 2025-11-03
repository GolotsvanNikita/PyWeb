from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import random
from datetime import datetime

from Project33.settings import DEBUG


# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)
def hello(request) :
    return HttpResponse("Hello, world!")


def home(request) :
    template = loader.get_template('home.html')
    context = {
        'x': 10,
        'y': 20,
        'page_title': 'Домашня',
        'page_header': 'Розробка вебдодатків з використанням Python',
        'time': datetime.now().strftime('%H:%M:%S')
    }
    return HttpResponse( template.render(context, request) )


def clonning(request) :
    template = loader.get_template('clonning.html')

    context =\
    {
        'time': datetime.now().strftime('%H:%M:%S')
    }

    return HttpResponse( template.render(context, request) )


def layouting(request) :
    template = loader.get_template('layouting.html')

    context =\
    {
        'time': datetime.now().strftime('%H:%M:%S')
    }

    return HttpResponse( template.render(context, request) )


def statics(request):
    template = loader.get_template('statics.html')

    context =\
    {
        'time': datetime.now().strftime('%H:%M:%S')
    }

    return HttpResponse(template.render(context, request))


def lottery(request):
    template = loader.get_template('lottery.html')

    random_numbers = random.sample(range(1, 42), 6)

    context =\
    {
        'rand': random_numbers,
        'time': datetime.now().strftime('%H:%M:%S')
    }

    return HttpResponse(template.render(context, request))
