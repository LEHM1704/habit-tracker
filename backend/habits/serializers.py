from rest_framework import serializers
from .models import Habit, HabitRecord


class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = ['id', 'habit', 'date', 'completed', 'note']
        read_only_fields = ['id']


class HabitSerializer(serializers.ModelSerializer):
    records=HabitRecordSerializer(many=True, read_only=True)
    
    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'description', 'frequency', 'records','created_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'created_at', 'updated_at','user']