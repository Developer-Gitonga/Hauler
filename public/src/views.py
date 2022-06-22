from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.

def contact(request):
  
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      Movingfrom = form.cleaned_data['Movingfrom']
      MovingTo = form.cleaned_data['MovingTo']
      
      print(Movingfrom, MovingTo)
    
  form = ContactForm()
  return render(request,"form.html", {'form' :form})
  
