from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from UserApp.models import User
from .models import CalendarModel

class CalendarView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        #user_id = User.objects.get(id=request.user.i)
        request.data['user'] = request.user.id
        serializer = CalendarSerializer(data=request.data)
        
        if serializer.is_valid():
            
            try: 
                event = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)