from django.contrib import admin
from .models import Users,Profile

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','phone_No','username')
    
    
    
admin.site.register(Users, CustomUserAdmin)




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','email_verified','email_code',
                    'location','state','admission', 'fullname')
    
    
    
admin.site.register(Profile, ProfileAdmin)
    