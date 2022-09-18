from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def hompage(request):
    return render(request, 'home.html')



def my_functional_view(request):
    massage = ''
    if request.method == "POST":
      
      username = request.POST['username']
      name = request.POST['name']
      email = request.POST['email']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      if len(username) < 6:
            massage = "Your username is too short"
      elif User.objects.filter(username=username):
            massage ='This username is already taken'      
      elif len(email)< 6:
            massage = "Please enter true email address"  
      elif User.objects.filter(email=email):
            massage = "You have already an account according to your email address"      
      elif len(password1)<6:
            massage = "The password must contain 6 symbols"
      elif password1 != password2:
            massage = "The passwords don't match"    
      else:                 
            user = get_user_model().objects.create(first_name = name, username=username, password=make_password(password1), email=email)
            user.is_active = False  # Example
            user.is_staff = False
            send_email(user)
            return redirect('confirm_needed', user.id)
      
      
    return render(request, 'registration/signup.html', {"massage":massage})




def confirm_needed(request, id):
      user = User.objects.get(id=id)
      if user.is_active == True:
            return redirect('/login')
      else:
            return render(request, 'confirm_needed.html')