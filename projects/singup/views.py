from django.views.generic import View
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login
from .models import  Profile
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model



Users = get_user_model()

# Create your views here.
class Singup(View):
    def get(self, request):
       
      


        #    return render(request, 'signup/signup.html')
           


       return render(request, 'signup/signup.html')
        




    def post(self, request):
       email  = request.POST['email']
       username = request.POST['username']
       if  Users.objects.filter(email=email).exists():
           return HttpResponse('emails exist')
       if  Users.objects.filter(username=username).exists():
           return HttpResponse('username exist')
       user = Users.objects.create_user(email=email, username=username)
       user_profile =  Profile.objects.create(user=user)
       generate_verfication = get_random_string(length=6)
       user_profile.email_code = generate_verfication 
       user_profile.save()
       return HttpResponse('created account')
       return render(request, 'signup/signup.html')
