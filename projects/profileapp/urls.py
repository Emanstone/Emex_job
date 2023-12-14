from django.urls import path
from .views import ProfilePage, EditProfilePage


urlpatterns = [

    path('', ProfilePage.as_view(),name='profile'),
    path('proedit/', EditProfilePage.as_view(), name='proeditor'),    
]