from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import inline_serializer
from .services import *
from .selectors import *
from .serializer import *

class ExerciseCreateApi(APIView):
    class ExerciseInputSerializer(serializers.Serializer):
        days = DaySerializer(many=True)
        image = serializers.ImageField()
        name = serializers.CharField(max_length=50)
        times = serializers.IntegerField()
        level = serializers.IntegerField()
    
    @extend_schema(
            operation_id='CreateExercise',
            request=ExerciseInputSerializer,
            responses={201: ExerciseSerializer,
            400: inline_serializer(
                name="ExerciseCreateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Exercise']
        )   
    def post(self, request):
        try:
            serializer = self.ExerciseInputSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            exercise = exercise_create(**serializer.validated_data)
            output_serializer = ExerciseSerializer(exercise)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ExerciseUpdateApi(APIView):
    class ExerciseUpdateInputSerializer(serializers.Serializer):
        image = serializers.ImageField()
        name = serializers.CharField(max_length=50)
        times = serializers.IntegerField()
        level = serializers.IntegerField()
    
    @extend_schema(
            operation_id='CreateExercise',
            request=ExerciseUpdateInputSerializer,
            responses={201: ExerciseSerializer,
            400: inline_serializer(
                name="ExerciseUpdateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Exercise']
        )
    def put(self, request, exercise_id):
        try:
            serializer = self.ExerciseUpdateInputSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            exercise = exercise_update(**serializer.validated_data, exercise_id=exercise_id)
            output_serializer = ExerciseSerializer(exercise)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetailApi(APIView):
    class ExerciseOutputSerializer(serializers.Serializer):
        days = DaySerializer(many=True)
        image = serializers.ImageField()
        name = serializers.CharField(max_length=50)
        times = serializers.IntegerField()
        level = serializers.IntegerField()
        
    @extend_schema(
            operation_id='Exercise Detail',
            responses={200:ExerciseOutputSerializer},
            tags=['Exercise']
        )   
    def get(self, request, exercise_id):
        try:
                exercise = exercise_view(id=exercise_id)
                serializer = self.ExerciseOutputSerializer(exercise)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:        
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DayCreateApi(APIView):
    class DayInputSerializer(serializers.Serializer):
        program = serializers.IntegerField()
    
    @extend_schema(
            operation_id='CreateExercise',
            request=DayInputSerializer,
            responses={201: DaySerializer,
            400: inline_serializer(
                name="ExerciseCreateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Day']
        )   
    def post(self, request):
        try:
            serializer = self.DayInputSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            day = day_create(**serializer.validated_data)
            output_serializer = DaySerializer(day)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DayUpdateApi(APIView):
    class DayUpdateInputSerializer(serializers.Serializer):
        program = serializers.IntegerField()
    
    class DayPatchSerializer(serializers.Serializer):
        exercises = ExerciseSerializer(many=True)
        
    @extend_schema(
            operation_id='CreateExercise',
            request=DayUpdateInputSerializer,
            responses={201: DaySerializer,
            400: inline_serializer(
                name="ExerciseCreateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Day']
        )   
    def put(self, request, day_id):
        try:
            serializer = self.DayUpdateInputSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            day = day_update(**serializer.validated_data, day_id=day_id)
            output_serializer = DaySerializer(day)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
            operation_id='CreateExercise',
            request=DayPatchSerializer,
            responses={201: DaySerializer,
            400: inline_serializer(
                name="ExerciseCreateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Day']
        )  
    def patch(self, request, day_id):
        try:
            serializer = self.DayPatchSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            day = day_add_exercises(**serializer.validated_data, day_id=day_id)
            output_serializer = DaySerializer(day)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DayDetailApi(APIView):
    class DayOutputSerializer(serializers.Serializer):
        program = ProgramSerializer()
        exercises = ExerciseSerializer(many=True)
        
        
    @extend_schema(
            operation_id='Exercise Detail',
            responses={200:DayOutputSerializer},
            tags=['Day']
        )   
    def get(self, request, day_id):
        try:
                day = day_view(id=day_id)
                serializer = self.DayOutputSerializer(day)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:        
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProgramCreateApi(APIView):
    class ProgramInputSerializer(serializers.Serializer):
        name = DaySerializer(many=True)
        level = serializers.IntegerField()
        careted_by = serializers.IntegerField()
        duration_failed = serializers.IntegerField()
    
    @extend_schema(
            operation_id='CreatePrgram',
            request=ProgramInputSerializer,
            responses={201: ExerciseSerializer,
            400: inline_serializer(
                name="ProgramCreateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Program']
        )   
    def post(self, request):
        try:
            serializer = self.ProgramInputSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            exercise = program_create(**serializer.validated_data)
            output_serializer = ProgramSerializer(exercise)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProgramUpdateApi(APIView):
    class ProgramUpdateInputSerializer(serializers.Serializer):
        name = DaySerializer(many=True)
        level = serializers.IntegerField()
        careted_by = serializers.IntegerField()
        duration_failed = serializers.IntegerField()
    
    @extend_schema(
            operation_id='CreateProgram',
            request=ProgramUpdateInputSerializer,
            responses={201: ExerciseSerializer,
            400: inline_serializer(
                name="ProgramUpdateFailed",
                fields={
                    "Error": serializers.CharField(default="string"),
                },
            )
            },
            tags=['Program']
        )
    def put(self, request, program_id):
        try:
            serializer = self.ProgramUpdateInputSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            program = program_update(**serializer.validated_data, program_id=program_id)
            output_serializer = ProgramSerializer(program)
            return Response(output_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProgramDetailApi(APIView):
    
        
    @extend_schema(
            operation_id='Exercise Detail',
            responses={200:ProgramSerializer},
            tags=['Exercise']
        )   
    def get(self, request, program_id):
        try:
                program = program_view(id=program_id)
                serializer = ProgramSerializer(program)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:        
            return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
  