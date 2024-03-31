from rest_framework import serializers
from .models import *

class CalendarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CalendarModel
        fields = '__all__'
    
    def validate(self, data):
        
        user = data.get('user')
        date = data.get('date')
        start_hour = data.get('start_hour')
        end_hour = data.get('end_hour')
        
        #verificar si ya existe un evento para esa hora y dia
        existing_events = CalendarModel.objects.filter(
            user=user,
            date=date,
            start_hour__lt=end_hour,
            end_hour__gt=start_hour
        )
        
        if existing_events.exists():
            raise serializers.ValidationError("Ya existe un evento para este rango de horas en este día.")
        
        return data