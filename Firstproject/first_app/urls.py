from django.contrib import admin
from django.urls import path, include
from .views import hello, page2, page3, page4, page5

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', hello),
    path('Stream', page2),
    path('Donations', page3),
    path('Users', page4),
    path('Info', page5),
]