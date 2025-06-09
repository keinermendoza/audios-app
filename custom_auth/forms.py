from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .widgets import CustomPasswordInput

class LoginCustomUser(AuthenticationForm):
    password = forms.CharField(
        label="Introduce tu Contraseña",
        widget=CustomPasswordInput
    ) 

class RegisterCustomUser(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = CustomPasswordInput()
        self.fields['password2'].widget = CustomPasswordInput()

