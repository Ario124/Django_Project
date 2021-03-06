from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, Offer, LandType
from .forms import UserRegisterForm, OfferForm



##  home page displaying offers  ##
def home(request):
    offers = Offer.objects.all()
    landtype = LandType.objects.all()
    context = {'offers': offers, 'landtype': landtype}
    return render(request, 'project/home.html', context)


##  login user  ##
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


##  logout user  ##
def logoutPage(request):
    logout(request)
    return redirect('home')


##  register user  ##
def registerPage(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'project/login_register.html', {'form': form})



##  Will display available offers  ##
def offerPage(request, pk):
    landtype = LandType.objects.all()
    offers = Offer.objects.get(id=pk)
    offers.views += 1
    offers.save()
    context = {'offer': offers, 'landtype':landtype}
    return render(request, 'project/offer.html', context)

## To prevent users from creating offers when not logged in. ##
@login_required(login_url='login')
def createofferPage(request):
    form = OfferForm()

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'project/create_offer.html', context)

## To prevent users from updating offers when not logged in, it also check to see if user is the host of the offer. Only host can update. ##
@login_required(login_url='login')
def updateOffer(request, pk):
    offer = Offer.objects.get(id=pk)
    form = OfferForm(instance=offer)
    if request.user != offer.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        offer.name = request.POST.get('name')
        offer.description = request.POST.get('description')
        offer.location = request.POST.get('location')
        offer.price = request.POST.get('price')
        offer.area = request.POST.get('area')
        offer.save()
        return redirect('home')

    context = {'form': form, 'offer': offer}
    return render(request, 'project/update_offer.html', context)

def propertyType(request):
    property_type = CharField(max_length=100)
    return render(request, 'project/property_types.html', {'property_type': property_type})


## To prevent users from deleting offers when not logged in, it also check to see if user is the host of the offer. Only host can delete. ##
@login_required(login_url='login')
def deleteOffer(request, pk):
    offer = Offer.objects.get(id=pk)

    if request.user != offer.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        offer.delete()
        return redirect('home')
    return render(request, 'project/delete_offer.html', {'obj': offer})