from http.client import responses

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor
from .serializer import DoctorSerializer


@api_view(['GET'])
def doctor_list(request):
    doctors = Doctor.objects.all()
    serializer= DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def doctor_detail(request, pk):
   try:
       doctor = Doctor.objects.get(pk=pk)
   except Doctor.DoesNotExist:
       return Response({"error : Not Found"},status=404)

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
       return Response({"message" : "deleted"})
