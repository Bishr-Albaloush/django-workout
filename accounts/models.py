from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user')
    image = models.ImageField(upload_to='profile/')
    blankDuration = models.IntegerField()
    pushUpNumbers = models.IntegerField()
    tall = models.IntegerField()
    weight = models.IntegerField()
    fatPercentage = models.IntegerField()
    level = models.IntegerField(blank=True, null=True,)
    def __str__(self):
        return str(self.user)


