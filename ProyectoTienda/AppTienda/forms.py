from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)

    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")