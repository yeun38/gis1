from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(args):
    pass


def hello(request):
    return render(request , 'accountapp/hello_world.html')