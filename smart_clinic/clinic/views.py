from http.client import responses

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Patient, Appointment
from .serializer import DoctorSerializer, PatientSerializer, AppointmentSerializer


@api_view(['GET'])
def doctor_list(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response({"error : Not Found"}, status=404)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # render is for HTML files, Response is for API data.
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        doctor.delete()
        return Response({"message": "deleted"})


# patient view
@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({"error : Not Found"}, status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        patient.delete()
        return Response({"message": "deleted"})


# appointment view
@api_view(['GET'])
def appointment_list(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({"error : Not Found"}, status=404)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        appointment.delete()
        return Response({"message": "deleted"})
