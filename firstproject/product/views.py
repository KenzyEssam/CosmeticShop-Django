from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Product,Category_header
from .forms import CommentForm

# Create your views here.

def categories(request):
    products = Product.objects.all()
    category_headers = Category_header.objects.all()
    context = {'products': products , 'category_headers': category_headers}


    return render(request,'product/categories.html', context)


def productinfo(request , slug):
    product = Product.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()

            return redirect('productinfo', slug=product.slug)
    else:
        form = CommentForm()
        context = {'product': product , 'form': form}

    return render(request,'product/productinfo.html' , context)

