from django.urls import path
from .views import Signup, Verify, Register, Dashboard, Login, Logout


urlpatterns = [

    path('', Signup.as_view(),name='signup'),
    path('verifier/', Verify.as_view(), name='verifyit'),
    path('registra/', Register.as_view(), name='registerit'),
    path('dashb/', Dashboard.as_view(), name='dash'),
    path('log/', Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    
]
