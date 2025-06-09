from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .widgets import CustomPasswordInput

User = get_user_model()

class LoginCustomUser(AuthenticationForm):
    password = forms.CharField(
        label="Introduce tu Contraseña",
        widget=CustomPasswordInput
    ) 
class EditCustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nombre", "apellido", "_profile_image", "telefono"]

class RegisterCustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = CustomPasswordInput()
        self.fields['password2'].widget = CustomPasswordInput()

    def save(self, commit=True):
        """
        Agregado temporalmente hasta implementar la validacion por email con SMTP
        """
        # instancia en memoria
        user = super().save(commit=False) 
        
        # normalizo el dominio del email
        email = self.cleaned_data["email"]
        user.email = self.Meta.model.objects.normalize_email(email) 
        
        # temporalmente activando usuario al crear
        user.is_active = True 
        
        user.save() 
        return user

