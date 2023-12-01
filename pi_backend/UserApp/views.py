from rest_framework.views import APIView
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from django.db import IntegrityError
from django.conf import settings
from .serializers import *
from .models import User



#registro de usuario en la API   
class RegisterView(APIView):
    
    #parsear la clase para poder obtener las imagenes
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            user.save()
            
            return Response({'message':'Usuario Registrado, verifica tu cuenta'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


