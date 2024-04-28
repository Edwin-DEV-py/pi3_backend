from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FileApp.models import FileModel
from FileApp.serializers import FileSerializer
from .serializers import *
from .models import *
from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
import os

class GetFolderByParentId(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request,parentFolder=0):
        
        user = request.user
        
        folder = FolderModel.objects.filter(parentFolder=parentFolder, userId=user)
        serializer_folder = FolderSerializer(folder, many=True)
        
        files = FileModel.objects.filter(folderParent=parentFolder, userId=user)
        serializer_files = FileSerializer(files, many=True)
        
        combined_data = []
        
        for folder_data in serializer_folder.data:
                folder_data['type'] = 'folder'
                combined_data.append(folder_data)
            
        for file_data in serializer_files.data:
            file_data['type'] = 'file'
            
            #obtener la extensiond el archivo
            file_name = file_data['fileName']
            file_extension = os.path.splitext(file_name)[1].lstrip('.')
            file_data['extension'] = file_extension
            
            combined_data.append(file_data)
        
        return Response({'data': combined_data})