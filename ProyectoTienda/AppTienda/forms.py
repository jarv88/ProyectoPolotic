from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)

    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")


class NuevoProductoForm(forms.Form):
    titulo = forms.CharField(label="Nombre", max_length=50, required=True)
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripcion")
    imagen = forms.ImageField()
    

#Form creado para extraer la imagen y que sirva el Upload_to
#Sin el form no se guardaba en la carpeta media por lo que al querer mostrar no habia imagen
class ImagenUploadForm(forms.Form):
    
    imagen = forms.ImageField()


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'usuario'}), max_length=150, required=True, help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(), max_length=30, required=True, help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')
    first_name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'nombre'}), max_length=30, required=False, help_text='Opcional.')
    last_name = forms.CharField(
        label='Apellido', widget=forms.TextInput(attrs={'class': 'apellido'}), max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True, help_text='Se requiere una direccion de email valida.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )