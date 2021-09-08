from django.shortcuts import render

# Create your views here.
from .models import Rango
from .serializers import RangoSerializer
from rest_framework import generics

class RangoListCreate(generics.ListCreateAPIView):
    queryset = Rango.objects.all()
    serializer_class = RangoSerializer