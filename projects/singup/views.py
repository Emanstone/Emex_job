from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login
from .models import  Profile
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from projects.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.contrib import messages


# Create your views here.
Users = get_user_model()

class Signup(View):

    def get(self, request):

       return render(request, 'signing/signup.html')
        


    def post(self, request):
       email  = request.POST['email']
       username = request.POST['username']
       if  Users.objects.filter(email=email).exists():
           return HttpResponse('email exist')
       if  Users.objects.filter(username=username).exists():
           return HttpResponse('username exist')
       user = Users.objects.create_user(email=email, username=username)
       user_profile =  Profile.objects.create(user=user)

      # generate_verfication = get_random_string(length=6)
       generate_verfication = random.randint(100000, 999999)
       user_profile.email_code = generate_verfication 
       user_profile.save()

       subject = "otp verification"
       body = f"your verification code is: {generate_verfication}"
       from_email = EMAIL_HOST_USER
       toemail =  email
       send_now = send_mail(subject, body,from_email, [toemail])
       if send_now:
           messages.success(request, 'Successful, Verify your email here')
           return redirect('verifyit')
        #    context = {'user_profile': user_profile}
        #    return HttpResponse('sent email, check your inbox')
       return render(request, 'signup.html') 
           
           
       
        


class Verify(View):

    def get(self, request):
        
        return render(request, 'signing/verifier.html')



    def post(self, request):
        entered_otp = request.POST['otp']
        try: 
            user_profile_code = Profile.objects.get(email_code=entered_otp)
        except: user_profile_code = None   

        if user_profile_code:
           user_profile_code.email_verified = True

           user_profile_code.save()
           login(request, user_profile_code.user)
           messages.success(request, 'Success,You are logged in..Create your account here')
           return redirect('registerit')
        else:
            # return HttpResponse('verification code is invalid')
            messages.error(request, 'verification code is invalid')
    




class Register(View):

    def get(self, request):
        
        return render(request, 'signing/register.html')

    def post(self, request):
        # Ensure the user is logged in
        if not request.user.is_authenticated:
            # return HttpResponse('user_not_authenticated')
            messages.error(request, 'user_not_authenticated')

        # Retrieve the logged-in user
        user = request.user

        # Retrieve the username entered in the form
        entered_username = request.POST.get('username')
        entered_email = request.POST.get('email')

        # Check if the entered username matches the username of the logged-in user
        if entered_username != user.username:
            # return HttpResponse('username_mismatch')
            messages.error(request, 'username mismatch')
        
        if entered_email != user.email:
            # return HttpResponse('email_mismatch')
            messages.error(request, 'email mismatch')

        # Update user fields
        user.fullname = request.POST['fullname']
        user.phone_No = request.POST['phone_Number']
        user.location = request.POST['location']
        user.state = request.POST['state']

        # Check if passwords match
        password = request.POST['password']
        confirm_password = request.POST['password2']
        if password and password == confirm_password:
            user.set_password(password)

        user.save()

        # Retrieve user profile
        user_profile, profile_created = Profile.objects.get_or_create(user=user)

        # Update user profile fields
        user_profile.fullname = user.fullname
        user_profile.phone_N0 = user.phone_No
        user_profile.location = user.location
        user_profile.state = user.state
        user_profile.save()

        # Log in the user with updated information
        login(request, user)

        # Redirect to the dashboard page
        messages.success(request, 'Welcome to you Dashboard, proceed to update your profile')
        return redirect('dash')



    

class Dashboard(View):

    def get(self, request):
        user = request.user
        # tasks = user.tasks.all()
        # admission_status = user.admission_status

        context = {
            'user': user,
            # 'tasks': tasks,
            # 'admission_status': admission_status,
        }
       
        return render(request, 'signing/dash.html', context)


    def post(self, request):
        # Handle form submission
        if request.method == 'POST':
            pass
    





class Login(View):
    def get(self, request):
        return render(request, 'signing/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Retrieve the user by email
            user = Users.objects.get(email=email)

            # Check if the user is a superuser
            if user.is_superuser and user.check_password(password):
                # Log in the superuser if password match
                login(request, user)
                messages.success(request, 'Welcome back')
                return redirect('dash')
            if not password:
                messages.error(request, 'Invalid input')
                return redirect('login')

            else:
                # For regular users, check email verification
                user_profile = Profile.objects.filter(user=user).first()
                
                if user_profile and not user_profile.email_verified:
                    verification_code = user_profile.email_code
                    subject = "otp verification"
                    body = f"your verification code is: {verification_code}"
                    from_email = EMAIL_HOST_USER
                    toemail = email
                    send_now = send_mail(subject, body, from_email, [toemail])
                    if send_now:
                        messages.error(request, 'Verify your email')
                        return redirect('verifyit')

                # if user_profile and user_profile.email_verified and not password:
                #     messages.success(request, 'Create your account')
                #     return redirect('registerit') 

                if password and email:
                    user = authenticate(request, email=email, password=password)
                    if user:
                        login(request, user)
                        messages.success(request, 'Welcome back', user)
                        return redirect('dash')
                    else:
                        messages.error(request, 'Invalid input')
                        return redirect('login')    

        except Users.DoesNotExist:
            # User not found, redirect to signup page
            messages.success(request, 'Sign up to get started')
            return redirect('signup')




def Logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')









# User = get_user_model()

# class Login(View):
#     template_name = 'signing/login.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = Users.objects.get(email=email)
#             user = authenticate(request, email=email, password=password)

#             if user:
#                 login(request, user)
#                 return redirect('dash')

#         except User.DoesNotExist:
#             return redirect('signup')

#         return render(request, self.template_name, {'error_message': 'Invalid login credentials'})








