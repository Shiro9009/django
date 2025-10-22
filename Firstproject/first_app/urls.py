from django.contrib import admin
from django.urls import path, include
from .views import hello, page2, page3

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', hello),
    path('Stream', page2),
    path('Donations', page3),
]