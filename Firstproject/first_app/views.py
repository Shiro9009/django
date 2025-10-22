from django.shortcuts import render, HttpResponse

def hello(requast):
    return render(requast, 'base.html', {'my_test': 'BOLT'})