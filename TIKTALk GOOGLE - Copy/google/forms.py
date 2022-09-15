from django import forms as Emailforms

#from django.forms import EmailInput

from django.forms import EmailInput 


class ContactForm(Emailforms.Form):
   email = Emailforms.EmailField(label= False , widget=Emailforms.EmailInput(attrs={'placeholder' :'Email or Phone', 'onclick' : 'bar()', 'onfocus' : "this.placeholder=''", 'pattern' : '^[a-zA-Z0-9]+@gmail\.com','id': 'email'}))
 
 
 