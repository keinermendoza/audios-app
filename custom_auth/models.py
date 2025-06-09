from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# # Create your models here.
# class MiAdministradorCuentas(BaseUserManager):
#     def create_user(self, nombre, apellido, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("El usuario debe tener una dirección de correo electrónico")
#         if not username:
#             raise ValueError("El usuario debe tener un Nombre de Usuario")
        
#         usuario = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             nombre=nombre,
#             apellido=apellido,
#             **extra_fields
#         )
        
#         usuario.set_password(password)
#         usuario.save(using=self._db)
#         return usuario
    
#     def create_superuser(self, nombre, apellido, username, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_admin", True)
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superadmin", True)

#         return self.create_user(
#             nombre=nombre, apellido=apellido, username=username, email=email, password=password, **extra_fields
#         )