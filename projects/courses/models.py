from django.db import models
from singup .models import Profile, Users

# Create your models here.


class Createcourse(models.Model):
    course = models.CharField(max_length=200, blank=True,null=True)
    description = models.TextField()
    upload_image = models.ImageField(upload_to='task')
    duration  = models.DateField(auto_now_add=True)
    whatsapp_group  = models.CharField(max_length=300,blank=True,null=True)
  

    def __str__(self):
        return self.course
    

class course(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    choose =  models.ForeignKey(Createcourse, on_delete=models.CASCADE)
    Reason = models.TextField()
    date = models.DateField(auto_created=True)
    work = models.CharField(max_length=200, blank=True, null=True)
    progress = models.IntegerField(default=0)  # Progress in percentage

    def __str__(self):
        return self.choose
    

class Contributor(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Courses = models.ForeignKey(Createcourse, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Collaborator(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    courses = models.ForeignKey(Createcourse, on_delete=models.CASCADE)
    About = models.TextField(max_length=500,blank=True, null=True)
    uplaod_profile =  models.ImageField(upload_to='profile')
    date = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.user