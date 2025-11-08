from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)

def clonning(request) :
    template = loader.get_template('clonning.html')
    return HttpResponse( template.render() )


def hello(request) :
    return HttpResponse("Hello, world!")


def home(request) :
    template = loader.get_template('home.html')
    context = {
        'x': 10,
        'y': 20,
        'page_title': 'Домашня',
        'page_header': 'Розробка вебдодатків з використанням Python'
    }
    return HttpResponse( template.render(context, request) )


def layouting(request) :
    template = loader.get_template('layouting.html')
    return HttpResponse( template.render() )


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
