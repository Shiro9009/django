from django.shortcuts import render, HttpResponse

def hello(requast):
    return render(requast, 'base.html', {'my_test': 'BOLT'})

def page2(requast):
    return render(requast, 'two.html')

def page3(requast):
    return render(requast, 'three.html')