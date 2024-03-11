from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#clase Manager para la creacion de usuarios
class Manager_account(BaseUserManager):
    def create_user(self,names,last_names,email,phone,avatar,password=None,):
        
        
        user = self.model(
            names = names,
            last_names = last_names,
            email = email,
            phone = phone,
            avatar = avatar,
        )
        
        user.set_password(password)
        user.is_active = True
        user.save(using = self._db)
        return user
    
    def create_superuser(self,names,last_names,email,phone,password):
        
        user = self.create_user(
            names = names,
            last_names = last_names,
            email = email,
            phone = phone,
            avatar=None
        )
        
        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

#clase del usuario
class User(AbstractBaseUser):
    
    #atributos
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,max_length=300)
    names = models.CharField(max_length=100)
    last_names = models.CharField(max_length=100)
    phone = models.IntegerField()
    avatar = models.ImageField(upload_to='imgs/profile_img', null=True)
    
    #atributos de django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    
    #roles de django
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names','last_names','phone']
    
    objects = Manager_account() #instanciamos la clase
    
    #valores a pintar al listar los usuarios
    def __str__(self):
        return self.last_names
    
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    
    def has_module_perms(self,add_label):
        return True
