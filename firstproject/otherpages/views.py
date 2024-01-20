from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog,Blog_slider
from .models import Team,AboutUs,Card
from .models import about_header
from .forms import ContactForm


# Create your views here.

def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
        context = {'form': form}

    return render(request,'otherpages/contact.html' , context)

def about(request):
    teams = Team.objects.all()
    about_headers = about_header.objects.all()
    about_uss = AboutUs.objects.all()
    cards = Card.objects.all()
    context = {'teams': teams , 'about_headers':about_headers , 'about_uss':about_uss , 'cards':cards}

    return render(request, 'otherpages/about.html', context)

def blog(request):
    blogs = Blog.objects.all()
    blog_sliders = Blog_slider.objects.all()

    return render(request, 'otherpages/blog.html',{'blogs': blogs , 'blog_sliders': blog_sliders})


