from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.template import loader
from .forms.demo_form import DemoForm
from .forms.styled_form import StyledForm
from .forms.delivery_form import DeliveryForm
from .forms.reg_form import RegForm
from datetime import datetime
from .models import User
import hashlib

# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)

def clonning(request) :
    template = loader.get_template('clonning.html')
    return HttpResponse( template.render() )


def form_delivery(request) :
    template = loader.get_template('form_delivery.html')
    if request.method == 'GET' :
        context = {
            'form': DeliveryForm()
        }
    elif request.method == 'POST' :
        form = DeliveryForm(request.POST)
        context = {
            'form': form
        }
    return HttpResponse( template.render(context=context, request=request) )


def form_styled(request) :
    template = loader.get_template('form_styled.html')
    if request.method == 'GET' :
        context = {
            'form': StyledForm()
        }
    elif request.method == 'POST' :
        form = StyledForm(request.POST)
        context = {
            'form': form
        }
    return HttpResponse( template.render(context=context, request=request) )


def forms(request) :
    if request.method == 'GET' :
        template = loader.get_template('forms.html')
        context = {
            'form': DemoForm()
        }
    elif request.method == 'POST' :
        form = DemoForm(request.POST)
        context = {
            'form': form
        }
        template = loader.get_template('form_ok.html' if form.is_valid() else 'forms.html')
    else :
        return HttpResponseNotAllowed()
    
    return HttpResponse( template.render(context=context, request=request) )


def hello(request) :
    return HttpResponse("Hello, world!")


def home(request) :
    template = loader.get_template('home.html')
    context = {
        'x': 10,
        'y': 20,
        'page_title': 'Домашня',
        'page_header': 'Розробка вебдодатків з використанням Python',
        'now': datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    }
    return HttpResponse( template.render(context, request) )


def layouting(request) :
    template = loader.get_template('layouting.html')
    return HttpResponse( template.render() )


def models(request) :
    template = loader.get_template('models.html')
    if request.method == 'GET' :
        context = {
            'form': RegForm()
        }
        context['dk'] = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=b'password',
            salt=b"123",
            iterations=1000000,
            dklen=16).hex()
    else :
        form = RegForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid() :
            form_data = form.cleaned_data
            user = User(
                first_name = form_data['first_name'],
                last_name  = form_data['last_name'],
                email      = form_data['email'],
                phone      = form_data['phone'],
                birthdate  = form_data['birthdate']
            )
            user.save()
            context['user'] = user
            context['dk'] = hashlib.pbkdf2_hmac(
                hash_name='sha256',
                password=form_data['password'],
                salt="123",
                iterations=1e6,
                dklen=32)
    return HttpResponse( template.render(request=request, context=context) )


def params(request) :    
    context = {
        'params': str(request.GET),
        'user': request.GET.get('user', 'Немає даних'),
        'q': request.GET.get('q', 'Немає даних'),
    }
    about = request.GET.get('about', None)
    if about == 'GET' :
        context['about_get'] = " (метод не має тіла і вживається як запит на читання)"
    elif about == 'POST' :
        context['about_post'] = " (метод може мати тіло і вживається як запит на створення)"
    '''Д.З. Створити посилання-підказки для НТТР-методів PUT, PATCH, DELETE
    (аналогічно створеним на занятті для методів GET, POST).
    До звіту додавати скріншоти'''
    template = loader.get_template('params.html')
    return HttpResponse( template.render(context, request) )


def statics(request) :
    template = loader.get_template('statics.html')
    return HttpResponse( template.render() )
