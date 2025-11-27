from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.template import loader
from .forms import demo_form
import random
from datetime import datetime
from .forms.forms import TaxiCarForm
from .forms.styled_form import StyledForm
from .forms.delivery_form import DeliveryForm
from .forms.signup_form import SignupForm
from .helper import *

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


def forms(request):
    if request.method == 'GET':
        template = loader.get_template('forms.html')
        context = \
        {
            'form': demo_form.DemoForm()
        }
    elif request.method == 'POST':
        form = demo_form.DemoForm(request.POST)
        template = loader.get_template('form_ok.html' if form.is_valid() else 'forms.html')

        context = \
        {
            'form': form
        }
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return HttpResponse(template.render(context=context, request=request))


def taxi_car(request):
    if request.method == 'GET':
        template = loader.get_template('taxi_car.html')
        context =\
        {
            'form': TaxiCarForm(),
            'time': datetime.now().strftime('%H:%M:%S')
        }
    elif request.method == 'POST':
        form = TaxiCarForm(request.POST)

        if form.is_valid():
            template = loader.get_template('taxi_car_ok.html')
            context =\
            {
                'data': form.cleaned_data,
                'time': datetime.now().strftime('%H:%M:%S')
            }
        else:
            template = loader.get_template('taxi_car.html')
            context =\
            {
                'form': form,
                'time': datetime.now().strftime('%H:%M:%S')
            }
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return HttpResponse(template.render(context=context, request=request))


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


def params(request):
    template = loader.get_template('params.html')

    context = \
        {
            'params': str(request.GET),
            'time': datetime.now().strftime('%H:%M:%S'),
            'user': request.GET.get('user', 'Data not found'),
            'q': request.GET.get('q', 'Data not found')
        }
    about = request.GET.get('about', None)
    if about == 'GET':
        context['about_get'] = "Method GET haven`t body and means like request on read"
    elif about == 'POST':
        context['about_post'] = "Method POST could have body and means like request on create"
    elif about == 'PUT':
        context['about_put'] = "Method PUT will have body and means like request on full update"
    elif about == 'PATCH':
        context['about_patch'] = "Method PATCH will have body and means like request on partial update"
    elif about == 'DELETE':
        context['about_delete'] = "Method DELETE may have body and means like request on delete"

    return HttpResponse(template.render(context, request))


def form_styled(request):
    template = loader.get_template('form_styled.html')
    if request.method == 'GET':
        context = \
            {
                'form': StyledForm()
            }
    elif request.method == 'POST':
        form = StyledForm(request.POST)

        context = \
            {
                'form': form
            }

    return HttpResponse(template.render(context=context, request=request))


def form_delivery(request):
    template = loader.get_template('form_delivery.html')
    if request.method == 'GET':
        context = \
            {
                'form': DeliveryForm()
            }
    elif request.method == 'POST':
        form = DeliveryForm(request.POST)

        context = \
            {
                'form': form
            }

    return HttpResponse(template.render(context=context, request=request))


def models(request):
    template = loader.get_template('models.html')
    return HttpResponse( template.render(request=request) )


def signup(request):
    template = loader.get_template('signup.html')
    if request.method == 'GET':
        context = \
            {
                'form': SignupForm()
            }
    elif request.method == 'POST':
        form = SignupForm(request.POST)

        context = \
            {
                'form': form,
                'is_ok': form.is_valid()
            }
    context['salt'] = salt()
    return HttpResponse( template.render(request=request, context=context) )


def lottery(request):
    template = loader.get_template('lottery.html')

    random_numbers = random.sample(range(1, 42), 6)

    context =\
    {
        'rand': random_numbers,
        'time': datetime.now().strftime('%H:%M:%S')
    }

    return HttpResponse(template.render(context, request))
