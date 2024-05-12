from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from .services import user_create, user_update, profile_update
from .selectors import profile_get
from .models import User
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import inline_serializer
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer 

class UserLoginApi(APIView):
    class LoginInputSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    @extend_schema(
        operation_id='login',
        description="Info about the login endpoint",
        request=LoginInputSerializer,
        responses={
            200: inline_serializer(
                name="LoginSuccessfull",
                fields={
                    "token": serializers.CharField(default="string"),
                    
                },
            ),
            400: inline_serializer(
                name="LoginFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            ),
            403:inline_serializer(
                name="LoginForbidden",
                fields={
                    "details": serializers.CharField(default="CSRF Failed: CSRF token from the 'X-Csrftoken' HTTP header incorrect."),
                },
            ),
        },
        tags=['auth']
    )
    def post(self, request):
        try:
            serializer = self.LoginInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            username = serializer.data['username']
            password = serializer.data['password']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_200_OK)
            else:
                return Response({"Error":"invalid login"},status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class UserCreateApi(APIView):
    class SignupInputSerializer(serializers.Serializer):
        email = serializers.CharField()        
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        password = serializers.CharField()
        blankDuration = serializers.DurationField(default="DD HH:MM:SS.uuuuuu")
        pushUpNumbers = serializers.IntegerField()
        tall = serializers.IntegerField()
        weight = serializers.IntegerField()
        fatPercentage = serializers.IntegerField()
        username = serializers.CharField()
        img = serializers.ImageField()

    
    @extend_schema(
            operation_id='SignUp',
            request=SignupInputSerializer,
            responses={201: inline_serializer(
                name="SignUpSuccessfull",
                fields={
                    "token": serializers.CharField(default="string"),
                },
            ),
            400: inline_serializer(
                name="SignUpFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['auth']
        )   
    def post(self, request):
        try:
            serializer = self.SignupInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            token = {"token":None}
            user, token["token"] = user_create(**serializer.validated_data)
            login(request, user)
            return Response(token, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutApi(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        parameters=[
            {
                "name": "Authorization",
                "description": "Authorization token",
                "required": True,
                "type": str,
                "location": "header",
            },
            # Add other custom headers here
        ],
        
        responses={
            200: inline_serializer(
                name="LogoutSuccessfull",
                fields={
                    "result_description": serializers.CharField(default="loged out successfully"),
                    
                },
            ),
            400: inline_serializer(
                name="LogoutFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
        },
        tags=['auth']
    )
    def get(self, request):
        try:
            logout(request)
            return Response({"result_description":"loged out successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailApi(APIView):
    class ProfileOutputSerializer(serializers.Serializer):
        user = UserSerializer()
        blankDuration = serializers.DurationField(default="DD HH:MM:SS.uuuuuu")
        pushUpNumbers = serializers.IntegerField()
        tall = serializers.IntegerField()
        weight = serializers.IntegerField()
        fatPercentage = serializers.IntegerField()
        image = serializers.ImageField()

    @extend_schema(
            operation_id='Profile Detail',
            responses={200:ProfileOutputSerializer},
            tags=['Profile']
        )   
    def get(self, request):
        try:
            if request.user.is_authenticated:
                profile = profile_get(user=request.user.id)
                serializer = self.ProfileOutputSerializer(profile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'Error':'User NOT Found'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:        
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class UserUpdateApi(APIView):
    class UserUpdateInputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        email = serializers.CharField()

    @extend_schema(
            operation_id='Update User',
            parameters=[
            {
                "name": "Authorization",
                "description": "Authorization token",
                "required": True,
                "type": str,
                "location": "header",
            },
            # Add other custom headers here
        ],
            request=UserUpdateInputSerializer,
            responses={202: inline_serializer(
                name="UserUpdateSuccessfull",
                fields={
                    "result_description": serializers.CharField(default="user updated successfull"),
                    
                },
            ),
                401:inline_serializer(
                name="UserUpdateFailed",
                fields={
                    "Error": serializers.CharField(default="User NOT Found"),
                    
                },
            ),
                400:inline_serializer(
                name="UserUpdateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                    
                },
            ),
                
                },
            tags=['User']
        )   
    def put(self, request):
        try:
            if request.user.is_authenticated:  
                serializer = self.UserUpdateInputSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                user_update(user_id=request.user.id, data = serializer.validated_data)

                return Response({'result_description':'user updated successfully'},status=status.HTTP_202_ACCEPTED)
            
            return Response({'Error':'User NOT Found'}, status=status.HTTP_401_UNAUTHORIZED)
                
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
                
class ProfileUpdateApi(APIView):    
    class ProfileUpdateInputSerializer(serializers.Serializer):
        blankDuration = serializers.DurationField(default="DD HH:MM:SS.uuuuuu") 
        pushUpNumbers = serializers.IntegerField()
        tall = serializers.IntegerField()
        weight = serializers.IntegerField()
        fatPercentage = serializers.IntegerField()
        image = serializers.ImageField()
    
    @extend_schema(
            operation_id='Update User',
            parameters=[
            {
                "name": "Authorization",
                "description": "Authorization token",
                "required": True,
                "type": str,
                "location": "header",
            },
            # Add other custom headers here
        ],
            request=ProfileUpdateInputSerializer,
            responses={202: inline_serializer(
                name="ProfileUpdateSuccessfull",
                fields={
                    "result_description": serializers.CharField(default="profile updated successfull"),
                    
                },
            ),
                401:inline_serializer(
                name="ProfileUpdateFailed",
                fields={
                    "Error": serializers.CharField(default="User NOT Found"),
                    
                },
            ),
                400:inline_serializer(
                name="ProfileUpdateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                    
                },
            ),
                
                },
            tags=['Profile']
        )
    def put(self, request):
        try:
            if request.user.is_authenticated:  
                serializer = self.ProfileUpdateInputSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                profile_update(profile_id=request.user.id, data = serializer.validated_data)

                return Response({'result_description':'profile updated successfully'},status=status.HTTP_202_ACCEPTED)
            return Response({'Error':'User NOT Found'}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as e:
            return Response({'Error':str(e)},status=status.HTTP_400_BAD_REQUEST)
