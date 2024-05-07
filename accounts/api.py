from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login
from .services import user_create, user_update, profile_update
from .selectors import profile_get
from .models import User
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, extend_schema_serializer
from drf_spectacular.types import OpenApiTypes
from rest_framework.permissions import IsAuthenticated

class UserCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.CharField()        
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        password = serializers.CharField()
        
        blankDuration = serializers.IntegerField()
        pushUpNumbers = serializers.IntegerField()
        tall = serializers.IntegerField()
        weight = serializers.IntegerField()
        fatPercentage = serializers.IntegerField()
        username = serializers.CharField()
        img = serializers.ImageField()
       
        
    @extend_schema(
            operation_id='Update Profile',
            request=InputSerializer,
            responses={200:status.HTTP_200_OK},
            tags=['User']
        )   
    def post(self, request):
        
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = {"token":None}
        user, token["token"] = user_create(**serializer.validated_data)
        login(request, user)
        return Response(token, status=status.HTTP_201_CREATED)

class UserUpdateApi(APIView):
    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()

    @extend_schema(
            operation_id='Update Profile',
            request=InputSerializer,
            responses={200:status.HTTP_200_OK},
            tags=['User']
        )   
    def post(self, request, user_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_update(user_id=user_id, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

class UserLogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class ProfileUpdateApi(APIView):
    
     
    class InputSerializer(serializers.Serializer):
        blankDuration = serializers.IntegerField()
        pushUpNumbers = serializers.IntegerField()
        tall = serializers.IntegerField()
        weight = serializers.IntegerField()
        fatPercentage = serializers.IntegerField()
        username = serializers.CharField()
        image = serializers.ImageField()
    
    @extend_schema(
            operation_id='Update Profile',
            request=InputSerializer,
            responses={200:status.HTTP_200_OK},
            tags=['Profile']
        )   
    def post(self, request, profile_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        profile_update(profile_id=profile_id, data = serializer.validated_data)

        return Response(status=status.HTTP_200_OK)

class ProfileDetailApi(APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        blankDuration = serializers.IntegerField()
        pushUpNumbers = serializers.IntegerField()
        tall = serializers.IntegerField()
        weight = serializers.IntegerField()
        fatPercentage = serializers.IntegerField()
        username = serializers.CharField()
        image = serializers.ImageField()
       
    @extend_schema(
            operation_id='Update Profile',
            responses={200:OutputSerializer},
            tags=['Profile']
        )   
    def get(self, request, profile_id):
        course = profile_get(id=profile_id)

        serializer = self.OutputSerializer(course)

        return Response(serializer.data)