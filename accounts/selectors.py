from .models import Profile

def profile_get(*,user):
    
    return Profile.objects.select_related('user').get(user = user)