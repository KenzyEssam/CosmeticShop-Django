from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery
from .models import Category
from .models import Header
from .models import Banner




# Create your views here.

def home(request):
    gallerys = Gallery.objects.all()
    categorys = Category.objects.all()
    headers = Header.objects.all()
    banners = Banner.objects.all()


    context = {'gallerys': gallerys , 'categorys': categorys , 'headers': headers , 'banners': banners}

    return render(request,'home/index.html' , context )

