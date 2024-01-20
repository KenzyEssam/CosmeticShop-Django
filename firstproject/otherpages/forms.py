from django import forms

from .models import Messagee

class ContactForm(forms.ModelForm):
    class Meta:
        model = Messagee
        fields = ['full_name','phone_number','email','message']