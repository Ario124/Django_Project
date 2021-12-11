from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User, Offer
from .forms import UserRegisterForm, OfferForm


def home(request):
    offers = Offer.objects.all()
    context = {'offers': offers}
    return render(request, 'project/home.html', context)

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'project/login_register.html', {'page':page})

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'project/login_register.html', {'form': form})



def offerPage(request, pk):
    offer = Offer.objects.get(id=pk)
    context = {'offer': offer}
    return render(request, 'project/offer.html', context)

def createofferPage(request):
    form = OfferForm()
    
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'project/create_offer.html', context)