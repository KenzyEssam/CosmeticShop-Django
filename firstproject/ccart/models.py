from django.db import models

# Create your models here.
class Checkouttt(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    credit_card_no = models.CharField(max_length=200)
    expiration_date = models.DateField("Expiration Date(mm/dd/yy)")
    submitt_date = models.DateTimeField()
