from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.


class Exercise(models.Model):
    image = models.ImageField(upload_to='exercise/')
    name = models.CharField(max_length=50)
    times = models.IntegerField()
    muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE)
    days = models.ManyToManyField('Day', related_name='exercise_day')
    def __str__(self):
        return str(self.name)

class Day(models.Model):
    program = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='program')

class Program(models.Model):
    name = models.CharField(max_length=50)
    duration_field = models.DurationField(default=timedelta(days=30))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)


class Practice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    duration = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)

class Muscle(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='muscle/')
    level = models.IntegerField(blank=True, null=True,)

    def __str__(self):
        return str(self.name)
    

    