from django.db import models
import os

def get_image_path(upload_image, image_file_name):
    return os.path.join("uploads", image_file_name)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    # image = models.FilePathField(path="employee_data/images")
    # upload_image = models.ImageField(upload_to=get_image_path, blank=True)   #specifies the subdirectory in uploads folder where the uploads will be saved 
    
