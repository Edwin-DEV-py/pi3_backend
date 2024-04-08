from django.db import models
from UserApp.models import User

class FolderModel(models.Model):

    #atributos
    id = models.AutoField(primary_key=True)
    folderName = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parentFolder = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folderName
