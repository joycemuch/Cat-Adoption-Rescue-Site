from django import forms 
from .models import Contacts


  
class ContactForm(forms.ModelForm):  
        class Meta:
            model = Contacts
            fields = "__all__"
            widgets = { 'Message' : forms.Textarea}

 

        # Name= forms.CharField(max_length=20)  
        # Email= forms.CharField(max_length=100)  
        # Message= forms.CharField(max_length=15)
            