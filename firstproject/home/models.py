from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to='static/img/')
    
    
class Category(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='static/img/') 


class Header(models.Model):
    title = models.TextField()
    body = models.TextField()
    image = models.CharField(max_length=200)  # or models.URLField() if it stores a URL

class Banner(models.Model):
    title = models.TextField()
    diss= models.TextField()
    body = models.TextField()
    image = models.CharField(max_length=200)  # or models.URLField() if it stores a UR