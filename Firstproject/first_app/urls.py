from django.contrib import admin
from django.urls import path, include
from .views import hello, page2, page3, page4, page5

urlpatterns = [
    path('', hello, name='hello'),
    path('Stream/', page2, name='page2'),
    path('Donations/', page3, name='page3'),
    path('Users/', page4, name='page4'),
    path('Info/', page5, name='page5'),
]