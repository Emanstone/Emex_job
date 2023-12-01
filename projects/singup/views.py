from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class Singup(View):
    def get(self, request):
       return render(request, 'signup/signup.html')
        




    def post(self, request):
         return render(request, 'signup/signup.html')
