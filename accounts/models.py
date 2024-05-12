from django.db import models
from django.contrib.auth.models import User
from exercise.models import Program
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user')
    image = models.ImageField(upload_to='profile/')
    blankDuration = models.DurationField()
    pushUpNumbers = models.IntegerField()
    tall = models.IntegerField()
    weight = models.IntegerField()
    fatPercentage = models.IntegerField()
    level = models.IntegerField(blank=True, null=True,)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank = True)
    def __str__(self):
        return str(self.user)


