
from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=250)
    dep_description=models.TextField()
    # dep_image=models.ImageField(upload_to='doctors')
