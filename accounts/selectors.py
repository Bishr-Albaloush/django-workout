from .models import Profile

def profile_get(*,id):
    return Profile.objects.get(id = id)