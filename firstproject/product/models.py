from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    current_price = models.TextField()
    old_price = models.TextField()
    desc = models.TextField()
    categ = models.TextField()
    stock=models.TextField()
    image = models.ImageField(upload_to='static/img/')
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        
        
class Category_header(models.Model):
    title = models.TextField()
    body = models.TextField()
    image = models.CharField(max_length=200) 
