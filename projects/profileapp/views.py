from django.views.generic import View
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from singup.models import Profile
from django.contrib import messages


# Create your views here.

Users = get_user_model()

class BaseProfileView(View):
    def get_profile_info(self, user):
        try:
            profile = user.profile  # Access the related Profile using the lowercased name
            profile_complete = bool(
                profile.location
                and profile.state
                and profile.fullname
                and profile.twitter_handle
                and profile.facebook_handle
                and profile.linkedin_handle
                and profile.current_digital_skills
                and profile.profile_image
                # and profile.user.current_digital_skills
            )

            profile_info = {
                'profile_image_url': profile.profile_image if profile.profile_image else None,
                'location': profile.location,
                'state': profile.state,
                'fullname': profile.fullname,
                'twitter_handle': profile.twitter_handle,
                'facebook_handle': profile.facebook_handle,
                'linkedin_handle': profile.linkedin_handle,
                'digital skills': profile.current_digital_skills,
                'user': profile.user,
            }

            return {'profile_info': profile_info, 'profile_complete': profile_complete}

        except Profile.DoesNotExist:
            return {}




class ProfilePage(LoginRequiredMixin, BaseProfileView):
    login_url = 'login'

    def get(self, request):
        context = self.get_profile_info(request.user)

        if not context:
            return redirect('signup')

        return render(request, 'Profile/profile.html', context=context)
    

    def post(self, request):
        # Process the submitted form data
        return render(request, 'Profile/profile.html')





class EditProfilePage(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return redirect('signup')

        context = {
            'profile_info': {
                'profile_image_url': user_profile.profile_image if user_profile.profile_image else None,
                'location': user_profile.location,
                'state': user_profile.state,
                'fullname': user_profile.fullname,
                'twitter_handle': user_profile.twitter_handle,
                'facebook_handle': user_profile.facebook_handle,
                'linkedin_handle': user_profile.linkedin_handle,
                'digital skills': user_profile.current_digital_skills,
            },

            'form_data': {
                # 'profile_image_url': user_profile.profile_image.url,
                # 'profile_image_url': user_profile.profile_image if user_profile.profile_image and user_profile.profile_image else None,   
                'state': user_profile.state,    
                'location': user_profile.location,   
                'fullname': user_profile.fullname,
                'twitter': user_profile.twitter_handle,
                'facebook': user_profile.facebook_handle,
                'linkedin': user_profile.linkedin_handle,
                'digital skills': user_profile.current_digital_skills,
            },
        }
        # print(request.FILES.get('profile_image_url'))
        return render(request, 'Profile/editprofile.html', context=context)



    def post(self, request):

        profile_image = request.FILES.get('postimage')
        location = request.POST.get('location')
        state = request.POST.get('state')
        fullname = request.POST.get('fullname')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        linkedin = request.POST.get('linkedin')
        current_digital_skills = request.POST.get('current_digital_skills')

        user = Profile.objects.get(user=request.user)

        # Get all form fields to be validated
        fields = {
            'location': location,
            'state': state,
            'fullname': fullname,
            'twitter_handle': twitter,
            'facebook_handle': facebook,
            'linkedin_handle': linkedin,
            'current_digital_skills': current_digital_skills
        }

        # Validate each field, ignoring empty fields and preventing 'none' values
        for field_value in fields.items():
            if field_value and field_value != 'none':
                if not field_value:
                    # If the field is empty, skip validation
                    continue


        # Process the uploaded profile image if any
        if profile_image:
            user.profile_image = profile_image
            user.save()

        # Update user information
        user.location = location
        user.fullname = fullname
        user.state = state
        user.twitter_handle = twitter
        user.facebook_handle = facebook
        user.linkedin_handle = linkedin
        current_digital_skills = current_digital_skills
        user.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('profile')

