from django.db import models
from singup .models import Profile, Users


# Create your models here.


admission_status = (

    ('pending', "pending"),
    ('approved', "approved")
)

# class Admission(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     date_applied = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(choices=admission_status, default='pending', max_length=200)
#     progress = models.IntegerField(default=0)  # In percentage

    # def __str__(self):
    #     return self.date_applied
    

class CreateTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_image = models.ImageField(upload_to='task')
    task_link  = models.CharField(max_length=200)

    def __str__(self):
        return self.description
    


class SubmitTask(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task = models.ForeignKey(CreateTask,on_delete=models.CASCADE)
    upload_screenshort = models.ImageField(upload_to='task')
    links  = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    progress = models.IntegerField(default=0)  # In percentage

    def __str__(self):
        return self.description