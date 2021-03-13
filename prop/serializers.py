from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class BuyAPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyAProperty
        fields = '__all__'