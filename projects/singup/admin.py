from django.contrib import admin
from .models import Users

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','phone_No','username')
    
    
    
admin.site.register(Users, CustomUserAdmin)
    