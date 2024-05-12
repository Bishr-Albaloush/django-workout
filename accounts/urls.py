from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import api
app_name = 'job'
urlpatterns = [
    path('api/v1/signup/',api.UserCreateApi.as_view(),name='signup'),
    path('api/v1/login/', api.UserLoginApi.as_view(),name='login'),
    path('api/v1/logout/', api.UserLogoutApi.as_view(),name='logout'),
    path('api/v1/user_update/',api.UserUpdateApi.as_view(),name='user_update'),
    path('api/v1/profile_update/',api.ProfileUpdateApi.as_view(),name='profile_update'),
    path('api/v1/profile_get/',api.ProfileDetailApi.as_view(),name='profile_get'),
]