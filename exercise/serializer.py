from rest_framework import serializers
from .models import *

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'days', 'image', 'times', 'level']

class MiniExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id']

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'program']

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'name', 'duration_field', 'level', 'created_by']
