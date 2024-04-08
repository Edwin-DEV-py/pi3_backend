from django.db import models
from UserApp.models import User
from FolderApp.models import FolderModel

class FileModel(models.Model):

    #atributos
    id = models.AutoField(primary_key=True, unique=True)
    fileName = models.CharField(max_length=200)
    folderParent = models.ForeignKey(FolderModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='files/', null=False)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fileName