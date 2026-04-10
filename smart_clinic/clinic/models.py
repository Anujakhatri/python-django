from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=40)
    Specialization = models.CharField(max_length=100)
    Experience = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

