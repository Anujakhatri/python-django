from django.db import models

# Create your models here.
class Doctor(models.Model):
    name= models.CharField(max_length=100)
    specialization= models.CharField(max_length=100)
    experience= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} → {self.doctor} on {self.date}"

