from django.shortcuts import render, HttpResponse
from .models import *

def hello(requast):
    return render(requast, 'base.html', {'my_test': 'BOLT'})

def page2(requast):
    streams = Streams.objects.all()
    return render(requast, 'two.html',  {'img': streams})

def page3(requast):
    return render(requast, 'three.html')
