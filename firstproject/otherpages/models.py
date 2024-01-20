from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    desc = models.TextField()
    creator = models.TextField()
    Day = models.IntegerField()
    Month=models.TextField()
    image = models.ImageField(upload_to='static/img/')

    date_added = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    name = models.TextField()
    job = models.TextField()
    image = models.ImageField(upload_to='static/img/')

    date_added = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-date_added'] 


class about_header(models.Model):
    title1 = models.TextField()
    title2= models.TextField()
    body = models.TextField()
    image = models.CharField(max_length=200) 
    
class AboutUs(models.Model):
    title = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='static/img/')

class Card(models.Model):
    title = models.TextField()
    icon = models.CharField(max_length=200) 

class Blog_slider(models.Model):
    title = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='static/img/')
    
class Messagee(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    message = models.TextField()

