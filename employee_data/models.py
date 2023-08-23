from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    image = models.FilePathField(path="employee_data/images")
    upload_image = models.ImageField(upload_to='./')   #specifies the subdirectory in uploads folder where the uploads will be saved 
    
