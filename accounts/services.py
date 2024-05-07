from django.contrib.auth.models import User
from .models import Profile
from common.services import model_update
from rest_framework.authtoken.models import Token





def profile_create(
    *,
    user:User,
    blankDuration: int,
    pushUpNumbers: int,
    tall: int,
    weight: int,
    fatPercentage: int,
    level: int,
    img: str,
    ) -> Profile:
    
    profile = Profile(user=user, weight=weight, fatPercentage=fatPercentage, blankDuration=blankDuration, pushUpNumbers=pushUpNumbers, tall=tall, image=img)
    profile.full_clean()
    profile.save()
    return profile


def user_create(
    email: str,
    first_name: str,
    last_name: str,
    username:str,
    password: str,
    blankDuration: int,
    pushUpNumbers: int,
    tall: int,
    weight: int,
    fatPercentage: int,
    img: str
    ) -> User:
    
    user = User(email=email, username=username, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.full_clean()
    user.save()
    token = Token.objects.create(user=user)
    

    profile_create(user=user, weight=weight, fatPercentage=fatPercentage, blankDuration=blankDuration, pushUpNumbers=pushUpNumbers, tall=tall, img=img)
    return user, token.key

def user_update(*, user_id: int, data) -> User:
    user = User.objects.get(id = user_id)
    non_side_effect_fields = ['first_name', 'last_name']

    user, has_updated = model_update(
        instance=user,
        fields=non_side_effect_fields,
        data=data
    )

    return user

def profile_update(*, profile_id: int, data):
    profile = Profile.objects.get(user = profile_id)
    non_side_effect_fields = ['blankDuration', 'pushUpNumbers', 'tall', 'weight', 'fatPercentage']
    
    profile, has_updated = model_update(
        instance=profile,
        fields=non_side_effect_fields,
        data=data
    )

    return profile

    
    
