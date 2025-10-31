from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

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
        'page_header': 'Розробка вебдодатків з використанням Python'
    }
    return HttpResponse( template.render(context, request) )


def clonning(request) :
    template = loader.get_template('clonning.html')
    return HttpResponse( template.render() )


def layouting(request) :
    template = loader.get_template('layouting.html')
    return HttpResponse( template.render() )
