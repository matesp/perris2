from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Crear usuarios
class PersonalizadoBaseUserManager(BaseUserManager):
    def create_user(self, email,password):
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Modelos
class Rescatado(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    raza = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='fotos/')

class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    fechanacimiento = models.DateField(blank=True,null=True)
    telefono = models.IntegerField(blank=True,null=True)
    email = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=40)
    comuna = models.CharField(max_length=40)
    vivienda = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = PersonalizadoBaseUserManager()

    def get_full_name(self):
        return self.username