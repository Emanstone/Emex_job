from django.db import models
from django.contrib.auth.models import AbstractUser
from .Usermanager import CustomUserManager



class Users(AbstractUser):
    email = models.EmailField(unique=True)
    password_optional = models.BooleanField(default=False)
    username = models.CharField(max_length=300, blank=True, null=True)
    phone_No = models.CharField(max_length=300, blank=True, null=True)


    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        # If password_optional is True, allow saving without a password
        if self.password_optional and not self.password:
            self._password = None
        super().save(*args, **kwargs)


admission_status = (

    ('on progrss', "on progrss"),
    ('approved', "approved")
)


class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    email_code = models.CharField(max_length=6, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=50)
    current_digital_skills = models.TextField(blank=True, null=True)
    twitter_handle = models.CharField(max_length=100, blank=True, null=True)
    facebook_handle = models.CharField(max_length=100, blank=True, null=True)
    linkedin_handle = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile')
    adminsion = models.CharField(choices=admission_status, default='on progrss', max_length=200)
    progress = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email



