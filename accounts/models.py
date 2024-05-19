from django.db import models
from django.contrib.auth.models import User
from exercise.models import Program, Muscle
# Create your models here.

FEED_BACK_CHOICES = [(1,"Foolproof"), (2,"Easy"), (3,"Normal"), (4,"Difficult"), (5,"Fiendish")]


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


class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    muscle = models.ForeignKey(Muscle, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.IntegerField(choices=FEED_BACK_CHOICES)


