from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import ContactForm 
from django.db import models
from .models import Contacts

# Create your views here.
def index(request):
      return render(request , 'index.htm')

import datetime

def home(request):
      if request.method == "POST":
            my_form = ContactForm(request.POST)
            if my_form.is_valid():
                  p = my_form.save()
                  p.Name = my_form.cleaned_data['Name']
                  
                  # return HttpResponse("submitted sucessfully")
                  return render(request , 'home.htm', {'form':my_form} )
            

      else:
          my_form = ContactForm()    
     
      return render(request , 'home.htm', {'form':my_form} )


def about(request):
      return render(request , 'about.htm')
