from django import forms
from django.contrib.auth.forms import UserCreationForm
from pagina.models import CustomUser
from pagina.models import Categoria

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingresa una dirección de correo válida.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        
        
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']


class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría',
                'style': 'font-size: 1rem; padding: 0.75rem;'
            }
        ),
        label='Nombre de la Categoría',
    )

    class Meta:
        model = Categoria
        fields = ['nombre']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': 'Este campo es obligatorio',
                'invalid': 'Por favor ingrese un valor válido'
            }