from dataclasses import field
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['id','name','author_name','message','email','auth_phno','date']