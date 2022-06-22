from django import forms

class ContactForm(forms.Form):
  Movingfrom = forms.CharField()
  
  MovingTo = forms.CharField()
  
  Size = forms.ChoiceField(choices=[('1 Room or small studio','1 Room or small studio'),('1 Bedroom apartment','1 Bedroom apartment'), ('2 Bedroom apartment','2 Bedroom apartment'),('3 Bedroom apartment','3 Bedroom apartment'),('4 Bedroom apartment','4 Bedroom apartment')])
  
  When  = forms.ChoiceField(choices=[('Unknown','Unknown'),('Within a week','Within a week'), ('1-2 months','1-2 months'),('2-4 months','2-4 months')])
  
  
  