from django import forms

from django.forms import PasswordInput


class PasswordFormss(forms.Form):
   password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder' :'Enter your password', 'name' : 'password','onclick' : 'gaga()','onfocus' : "this.placeholder=''",'class': 'password' ,'id' : 'password'}))
 