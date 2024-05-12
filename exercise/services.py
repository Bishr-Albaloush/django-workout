from models import *

def exercise_create(*,
    day:Day,
    name: str,
    times: str,
    level: str,
    image: str,)->Exercise:
    pass

def exercise_update(*,
    day:Day,
    name: str,
    times: str,
    level: str,
    image: str,)->Exercise:
    pass

def exercise_delete(*, exercise:Exercise):
    pass

def day_create(*, prgram:Program,
    excercises: list | []):
    pass

def day_update(*, prgram:Program,
    excercises: list | []):
    pass

def day_add_exercise(*, exercise:Exercise):
    pass

def day_delete_exercise(*, exercise: Exercise):
    pass

def day_delete(*, day: Day):
    pass

def program_create(*,
    name:str,
    feedback: int,
    duration_field: str,
    level: str,
    created_by: User,):
    pass

def program_update(*,
    name:str,
    feedback: int,
    duration_field: str,
    level: str,
    created_by: User,):
    pass

def program_add_day(*, day: Day):
    pass

def program_delete_day(*, day: Day):
    pass

def program_delete(*, program:Program):
    pass

def feedback_process(*, feedback:int):
    pass

def practice_create(*,
    user:User,
    exerxise: Exercise,
    program: Program,
    duration: str,
    created_at: str,):
    pass

def practice_update(*,
    user:User,
    exerxise: Exercise,
    program: Program,
    duration: str,
    created_at: str,):
    pass

def practice_delete(*, practice:Practice):
    pass

