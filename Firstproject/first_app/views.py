from django.shortcuts import render
from .models import *
from django.utils import timezone

def hello(request):
    current_stream = Streams.get_current_stream()
    return render(request, 'base.html', {'current_stream': current_stream})

def page2(request):
    streams = Streams.objects.all()
    return render(request, 'two.html', {'streams': streams})

def page3(request):
    donations = Donations.objects.all()
    return render(request, 'three.html', {'donations': donations})

def page4(request):
    users = Users.objects.all()
    return render(request, 'four.html', {'users': users})

def page5(request):
    user = Users.objects.first()
    return render(request, 'five.html', {'user': user})