from django.db import models
import os

def get_image_path(upload_image, image_file_name):
    return os.path.join("uploads", image_file_name)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
  
    
