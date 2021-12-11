from django.shortcuts import render



def home(request):
    return render(request, 'project/home.html')

def login(request):
    return render(request, 'project/login.html')