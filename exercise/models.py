from django.db import models
from django.contrib.auth.models import User

FEED_BACK_CHOICES = [(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5")]
# Create your models here.
class Exercise(models.Model):
    day = models.ManyToManyField('Day', related_name='exercise_day')
    image = models.ImageField(upload_to='profile/')
    name = models.CharField(max_length=50)
    times = models.IntegerField()
    level = models.IntegerField(blank=True, null=True,)
    def __str__(self):
        return str(self.user)


class Day(models.Model):
    program = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='program')

class Program(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    feedback = models.IntegerField(choices=FEED_BACK_CHOICES)

class Practice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exerxise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    duration = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)