from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
from .models import *
import base64

from Project33.settings import DEBUG


# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)
def hello(request) :
    return HttpResponse("Hello, world!")

def auth(request):
    authHeader = request.headers.get('Authorization')
    if not authHeader:
        return HttpResponse("Missing 'Authorization' header", status=401)
    authScheme = "Basic "
    if not authHeader.startswith(authScheme):
        return HttpResponse("Invalid 'Authorization' scheme", status=401)
    credentials = authHeader[len(authScheme):]
    if len(credentials) < 4:
        return HttpResponse("Credentials too short", status=401)
    try:
        user_pass = base64.b64decode(credentials).decode('utf-8')
    except binascii.Error as err:
        return HttpResponse("Credentials decode error" + str(err), status=401)
    parts = user_pass.split(':', maxsplit=1)
    if len(parts) != 2:
        return HttpResponse("User-pass decode error", status=401)
    login, password = parts
    try:
        access = Access.objects.get(login=login)
    except Access.DoesNotExist:
        return HttpResponse("Authorization rejected", status=401)
    _salt = access.salt
    _dk = dk(password, _salt)
    if _dk != access.dk:
        return HttpResponse("Authorization rejected.", status=401)
    return HttpResponse(login + ", " + password, status=200)

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


@csrf_exempt
def seed(request):
    if request.method == 'PATCH':
        res = \
            {
                "guest": "",
                "admin-role": "",
                "admin-user": "",
                "test-user": "",
                "test-access": ""
            }

        try:
            guest = Role.objects.get(name='Self registered')
        except Role.DoesNotExist:
            guest = Role()
            guest.name = 'Self registered'
            guest.save()
            res["guest"] = "created"
        else:
            guest.create_level = guest.read_level = guest.update_level = guest.delete_level = 0
            guest.save()
            res["guest"] = "updated"

        try:
            admin = Role.objects.get(name="Root Administrator")
        except Role.DoesNotExist:
            admin = Role()
            admin.name = 'Root Administrator'
            admin.save()
            res["admin-role"] = "created"
        else:
            admin.create_level = admin.read_level = admin.update_level = admin.delete_level = 1
            admin.save()
            res["admin-role"] = "updated"

        try:
            admin_user = User.objects.get(first_name="Default",
                                          last_name='Administrator')
        except User.DoesNotExist:
            admin_user = User()
            admin_user.first_name = "Default"
            admin_user.last_name = "Administrator"
            admin_user.email = 'admin@change.me'
            admin_user.phone = '0000000000'
            admin_user.save()
            res["admin-user"] = "created"
        else:
            res["admin-user"] = "updated"

        try:
            admin_access = Access.objects.get(user=admin_user)
        except Access.DoesNotExist:
            admin_access = Access()
            res["admin-access"] = "created"
        else:
            res["admin-access"] = "updated"

        _salt = salt()
        _dk = dk('root', _salt)
        admin_access.user = admin_user
        admin_access.role = Role.objects.get(name="Root Administrator")
        admin_access.login = 'admin'
        admin_access.salt = _salt
        admin_access.dk = _dk
        admin_access.save()

        try:
            test_user = User.objects.get(email='test_guest@mail.com')
        except User.DoesNotExist:
            test_user = User()
            test_user.first_name = "Test"
            test_user.last_name = "Guest"
            test_user.email = 'test_guest@mail.com'
            test_user.phone = '0000000000'
            test_user.save()
            res["test-user"] = "created"
        else:
            res["test-user"] = "updated"

        try:
            test_access = Access.objects.get(user=test_user)
        except Access.DoesNotExist:
            test_access = Access()
            test_access.user = test_user
            test_access.role = guest
            res["test-access"] = "created"
        else:
            res["test-access"] = "updated"

        t_salt = salt()
        t_dk = dk('1234', t_salt)

        test_access.login = 'guest_login'
        test_access.salt = t_salt
        test_access.dk = t_dk
        test_access.save()

        return JsonResponse(res)
    else:
        template = loader.get_template('seed.html')
        return HttpResponse(template.render())


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
        if form.is_valid():
            return render(request, 'form_delivery.html',
            {
                'success': True,
                'data': form.cleaned_data
            })
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
        if form.is_valid():
            form_data = form.cleaned_data
            _salt = salt()
            _dk = dk(form_data['password'], _salt)

            user = User()
            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.email = form_data['email']
            user.phone = form_data['phone_num']
            user.birthdate = form_data['birthdate']
            user.save()

            user_access = Access()
            user_access.user = user
            user_access.role = Role.objects.get(name='Self registered')
            user_access.login = form_data['login']
            user_access.salt = _salt
            user_access.dk = _dk
            user_access.save()

            context['user'] = user
            context['user_access'] = user_access
    # context['salt'] = salt()
    # context['dk'] = dk('123', '456')
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
