from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')

def next_page(request):
    return HttpResponse('Next page goes here')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('next_page/', next_page)
]
