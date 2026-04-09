from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet , ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Doctor, Patient, Appointment
from .serializer import DoctorSerializer, PatientSerializer, AppointmentSerializer

class DoctorViewSet(ModelViewSet):
   queryset = Doctor.objects.all()
   serializer_class = DoctorSerializer

   def get_queryset(self):
      queryset = Doctor.objects.all()
      specialization = self.request.query_params.get('specialization')
      if specialization:
         queryset = queryset.filter(specialization__icontains=specialization)
      return queryset


class PatientViewSet(ModelViewSet):
   queryset = Patient.objects.all()
   serializer_class = PatientSerializer


class AppointmentViewSet(ModelViewSet):
   queryset = Appointment.objects.all()
   serializer_class = AppointmentSerializer

   @action(detail=True, methods=['post'])
   def cancel(self, request, pk=None):
      appointment = self.get_object()
      appointment.status = 'cancelled'
      appointment.save()
      return Response({'status': 'Appointment cancelled'})

   @action(detail=True, methods=['patch'])
   def update_status(self, request, pk=None):
      appointment = self.get_object()
      new_status = request.data.get('status')
      appointment.status = new_status
      appointment.save()
      return Response({'status': f'Updated to {new_status}'})


class AdminViewSet(ReadOnlyModelViewSet):
   pass