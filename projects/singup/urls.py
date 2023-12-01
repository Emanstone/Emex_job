from django.urls import path
from .views import Singup


urlpatterns = [

    path('', Singup.as_view(),name='sigup')
    
]
