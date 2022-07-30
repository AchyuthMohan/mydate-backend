from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
    