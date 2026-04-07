from django.db import models

# Create your models here.
class Student(models.Model):
   name = models.CharField(max_length=100)
   subject = models.CharField(max_length=100)
   Roll = models.DecimalField(decimal_places=2, max_digits=10)
   created_at = models.DateTimeField(auto_now_add=True)
