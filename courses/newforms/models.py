from django.db import models

# Create your models here.

class students(models.Model):
        First_Name=models.CharField(max_length=20)
        USN= models.CharField(max_length=10)
        College=models.CharField(max_length=100)
        Course= models.CharField(max_length=100)
        Contact_Number= models.CharField(max_length=10)
        def __str__(self):
                return self.First_Name
