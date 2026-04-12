
from .serializers import RegistrationSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer=RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Registration successful')
    return Response(serializer.errors)
