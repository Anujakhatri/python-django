from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model) :
    APPOINTMENT_OPTIONS = [
        ('pending', 'Pending'), #(Raw database, Human Readable)
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete =models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices = APPOINTMENT_OPTIONS, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} → {self.doctor} on {self.date} "


