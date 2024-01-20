from django import forms
from django.utils import timezone
from .models import Checkouttt

class CheckOuttForm(forms.ModelForm):
    class Meta:
        model = Checkouttt
        fields = ['full_name', 'phone_number', 'address', 'credit_card_no', 'expiration_date']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.submitt_date = timezone.now()  # Set the current date and time
        if commit:
            instance.save()
        return instance