from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CheckOuttForm


# Create your views here.

def confirmation(request):
    return render(request, 'cart/confirmation.html')

def cart(request):
    return render(request,'cart/index.html')


def checkout(request):
    if request.method == 'POST':
        form = CheckOuttForm(request.POST)

        if form.is_valid():
            checkout_instance= form.save()
            submitt_date = checkout_instance.submitt_date
            address = checkout_instance.address

            return render(request ,'cart/confirmation.html',{'submitt_date':submitt_date , 'address': address})
    else:
        form = CheckOuttForm()
    return render(request,'cart/checkout.html' , {'form': form})