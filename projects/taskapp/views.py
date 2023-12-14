# from django.views.generic import View
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import get_user_model
# from .models import  Profile
# from django.core.mail import send_mail
# from projects.settings import EMAIL_HOST_USER
# from django.contrib import messages
# from .models import Admissions  
# from datetime import datetime


# # Create your views here.

# Users = get_user_model()


# class AdmissionProgress(View):

#     def get(self, request):
#         admission = Admissions.objects.filter(user=request.user).first()

#         if admission:
#             # Assuming you have a method to calculate progress based on completed tasks
#             progress = admission.calculate_progress()
#         else:
#             progress = 0

#         context = {'progress': progress, 'admission': admission}
#         return render(request, 'taskpage.html', context)

#     def post(self, request):
#         admission = Admissions.objects.filter(user=request.user).first()

#         if admission:
#             # Assuming you have a method to mark tasks as completed
#             admission.mark_task_as_completed()

#             # Update progress by adding 10% for each completed task
#             admission.progress += 10

#             # Update admission status based on progress
#             if admission.progress >= 100:
#                 admission.status = 'Approved'
#             else:
#                 admission.status = 'Pending'

#             # Update date applied if not already set
#             if not admission.date_applied:
#                 admission.date_applied = datetime.now()

#             admission.save()

#             messages.success(request, 'Task completed! Admission progress updated.')
#             return redirect('dash')  # Redirect to the same page or another as needed
#         else:
#             messages.error(request, 'Admission not found.')
#             return redirect('admission_apply')  # Redirect to the same page or another as needed










# views.py
# def register(request):
#     if request.method == 'POST':
#         email = request.POST['email']

#         # Create a user without setting a password
#         user = CustomUser.objects.create_user(email=email)

#         # Create a user profile
#         user_profile = UserProfile.objects.create(user=user)

#         # Generate verification code
#         verification_code = get_random_string(length=6)

#         # Save verification code in user profile
#         user_profile.email_verification_code = verification_code
#         user_profile.save()

#         # Send verification email
#         send_mail(
#             'Email Verification',
#             f'Your verification code is: {verification_code}',
#             'your_email@example.com',  # Replace with your sender email address
#             [email],
#             fail_silently=False,
#         )

#         return render(request, 'verification.html', {'user_profile': user_profile})

#     return render(request, 'register.html')

# def verify_email(request):
#     if request.method == 'POST':
#         verification_code = request.POST['verification_code']
#         user_profile = UserProfile.objects.filter(email_verification_code=verification_code).first()

#         if user_profile:
#             # Clear the verification code
#             user_profile.email_verification_code = None
#             user_profile.email_verified = True
#             user_profile.save()

#             # Log in the user
#             login(request, user_profile.user)

#             return redirect('set_password')  # Redirect to the page where the user sets a password
#         else:
#             # Handle incorrect verification code
#             return render(request, 'verification.html', {'error': 'Invalid verification code'})

#     return redirect('home')

# def set_password(request):
#     if request.method == 'POST':
#         password = request.POST['password']
#         user = request.user

#         # Set the password
#         user.set_password(password)
#         user.password_optional = False  # Mark that the password has been set
#         user.save()

#         return redirect('home')  # Redirect to the home page after setting the password

#     return render(request, 'set_password.html')
