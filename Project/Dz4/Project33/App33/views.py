from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)
def hello(request) :
    return HttpResponse("Hello, world!")


def home(request):
    template = loader.get_template('home.html')
    now = datetime.now()
    hour = now.hour
    hour_day = ''

    if 6 <= hour < 12:
        hour_day = 'Good Morning'
    elif 12 <= hour < 18:
        hour_day = 'Good Day'
    elif 18 <= hour < 22:
        hour_day = 'Good Evening'
    else:
        hour_day = 'Good Night'

    context =\
    {
        'x': 10,
        'y': 20,
        'page_title': 'Home',
        'page_header': 'Home Page',
        'time': datetime.now(),
        'gret': hour_day
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')

    context =\
    {
        'page_title': 'About',
        'page_header': 'About Page'
    }

    return HttpResponse(template.render(context, request))


def privacy(request):
    template = loader.get_template('privacy.html')

    context =\
    {
        'page_title': 'Privacy',
        'page_header': 'Privacy Page'
    }

    return HttpResponse(template.render(context, request))