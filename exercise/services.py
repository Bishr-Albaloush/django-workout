from models import *
from common.services import model_update

def exercise_create(*,
    day:Day,
    name: str,
    times: str,
    level: str,
    image: str,)->Exercise:
    exercise = Exercise(day=day, name=name, times=times, level=level, image=image)
    exercise.full_clean()
    exercise.save()
    return exercise

def exercise_update(*,
    exercise_id: int, data)->Exercise:
    exercise = Exercise.objects.get(id = exercise_id)
    non_side_effect_fields = ['day', 'name', 'times', 'level', 'image']
    
    exercise, has_updated = model_update(
        instance=exercise,
        fields=non_side_effect_fields,
        data=data
    )
    return exercise

def exercise_delete(*, exercise_id:int):
    exercise = Exercise.objects.delete(id=exercise_id)
    return True

def day_create(*, program:Program,
    excercises: list | []):
    day = Day(program = program)
    day.full_clean()
    day.save()
    
    for i in excercises:
        i.day.add(day)
        
    return day

def day_update(*,
    day_id: int, data):
    day = Day.objects.get(id = day_id)
    non_side_effect_fields = ['program']
    
    day, has_updated = model_update(
        instance=day,
        fields=non_side_effect_fields,
        data=data
    )
    return day

def day_add_exercises(*, day_id:int, exercises:list):
    day = Day.objects.get(id = day_id)
    for i in exercises:
        i.day.add(day)
        
    return day

def day_delete_exercises(*, day_id:int, exercises: Exercise):
    day = Day.objects.get(id = day_id)
    for i in exercises:
        i.day.remove(day)
        
    return day

def day_delete(*, day_id:int):
    day = Day.objects.delete(id=day_id)
    return True

def program_create(*,
    name:str,
    feedback: int,
    duration_field: str,
    level: str,
    created_by: User,)->Program:
    program = Program(name=name, feedback=feedback, duration_field=duration_field, level=level, created_by=created_by)
    program.full_clean()
    program.save()
    return program

def program_update(*,
    program_id, data)->Program:
    program = Program.objects.get(user = program_id)
    non_side_effect_fields = ['name', 'feedback', 'duration_field', 'level', 'created_by']
    
    program, has_updated = model_update(
        instance=program,
        fields=non_side_effect_fields,
        data=data
    )
    return program

""" def program_add_days(*, program_id: int, days:list):
    program = Program.objects.get(id = program_id)
    for i in days:
        i.program.add(program)
        
    return program """

""" def program_delete_day(*, day: Day):
    pass
"""

def program_delete(*, program_id:int):
    program = Program.objects.delete(id=program_id)
    return True

def feedback_process(*, feedback:int):
    pass

def practice_create(*,
    user:User,
    exerxise: Exercise,
    program: Program,
    duration: str,
    )->Practice:
    practice = Practice(user=user, exerxise=exerxise, program=program, duration=duration)
    practice.full_clean()
    practice.save()
    return practice

def practice_update(*,
    practice_id:int,
    data)->Practice:
    practice = Practice.objects.get(user = profile_id)
    non_side_effect_fields = ['user', 'exerxise', 'program', 'duration']
    
    practice, has_updated = model_update(
        instance=practice,
        fields=non_side_effect_fields,
        data=data
    )
    
    return practice

def practice_delete(*, practice_id:int):
    practice = Practice.objects.delete(id=practice_id)
    return True

