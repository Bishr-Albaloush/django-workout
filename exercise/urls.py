from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import api
app_name = 'exercise'
urlpatterns = [
    path('api/v1/create_exercise/',api.ExerciseCreateApi.as_view(),name='create_exercise'),
    path('api/v1/update_exercise/<int:exercise_id>',api.ExerciseUpdateApi.as_view(),name='update_exercise'),
    path('api/v1/get_exercise/<int:exercise_id>',api.ExerciseDetailApi.as_view(),name='get_exercise'),
      
    path('api/v1/create_day/',api.DayCreateApi.as_view(),name='create_day'),
    path('api/v1/update_day/<int:day_id>',api.DayUpdateApi.as_view(),name='update_day'),
    path('api/v1/get_day/<int:day_id>',api.DayDetailApi.as_view(),name='get_day'),
    
    path('api/v1/create_program/',api.ProgramCreateApi.as_view(),name='create_program'),
    path('api/v1/update_program/<int:program_id>',api.ProgramUpdateApi.as_view(),name='update_program'),
    path('api/v1/get_program/<int:program_id>',api.ProgramDetailApi.as_view(),name='get_program'),
    
]

 #       """ path('api/v1/login/', api.UserLoginApi.as_view(),name='login'),
 ##      path('api/v1/user_update/',api.UserUpdateApi.as_view(),name='user_update'),
   #     path('api/v1/profile_update/',api.ProfileUpdateApi.as_view(),name='profile_update'),
    #    path('api/v1/profile_get/',api.ProfileDetailApi.as_view(),name='profile_get'), """