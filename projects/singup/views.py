from django.views.generic import View
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login
from .models import  Profile
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from projects.settings import EMAIL_HOST_USER


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
       subject = "otp verification"
       body = f"your verification code is: {generate_verfication}"
       from_email = EMAIL_HOST_USER
       toemail =  email
       send_now = send_mail(subject, body,from_email, [toemail])
       if send_now:
           return HttpResponse('sent email, check your inbox')
           


      
       
       return render(request, 'signup/signup.html')
