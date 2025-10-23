from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)
def hello(request) :
    return HttpResponse("Hello, world!")
