from django import forms


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