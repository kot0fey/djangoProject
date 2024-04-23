from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.

def generate_string(request):
    if request.method == 'GET':
        name = request.GET.get("name")
        if name is None:
            name = "Recruto"
        message = request.GET.get("message")
        if message is None:
            message = "Давай дружить"
        response_string = "Hello "+ name +"! " + message + "!"
        return HttpResponse(response_string)
    else:
        return HttpResponseNotAllowed(['GET'])