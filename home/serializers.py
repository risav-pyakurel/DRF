from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['name','age'] # if we want to serialize all the fields we can also type '__all__'
        #exclude = [''] helps to exclude the fields we don't want to exclude