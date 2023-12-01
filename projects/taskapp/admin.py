from django.contrib import admin
from .models import CreateTask, SubmitTask

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','upload_image','task_link')
    

    
admin.site.register(CreateTask,TaskAdmin)
    