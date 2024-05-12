from models import Exercise, Day, Program, Practice
from django.db.models import Q

def exercise_view(*, id):
    return Exercise.objects.get(id=id)

def exercise_list(*, user):
    return Exercise.objects.all()

def day_view(*, id):
    return Day.objects.get(id=id)

def program_view(*, id):
    return Program.objects.get(id=id)

def practice_view(*, id):
    return Practice.objects.get(id=id)

def practice_list(*, user):
    return Exercise.objects.get(user=user)
