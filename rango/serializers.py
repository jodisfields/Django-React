from rest_framework import serializers
from .models import Rango

class RangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rango
        fields = ('id', 'Ship', 'Name', 'IP_Address' , 'Notes')