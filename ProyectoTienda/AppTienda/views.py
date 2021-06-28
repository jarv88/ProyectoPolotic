from django.shortcuts import render, redirect
from .models import Producto, CategoriaProd
from .forms import ContactForm
# Create your views here.
def index(request):
    productos=Producto.objects.all()
    return render(request,"AppTienda/index.html",{ "productos": productos })

def categorias(request):
    cat = CategoriaProd.objects.all()
    return render(request, "AppTienda/categorias.html", {"categorias": cat})

def acerca(request):
    return render(request, "AppTienda/acerca.html",)


def contacto(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")

            # send_mail(nombre,contenido,) otra forma
            #em = EmailMessage("Mensaje desde App",
            #                  "El usuario {}, email: {}, escribe: \n\n {}".format(nombre, email, mensaje),
            #                  "", ["joseangel038@gmail.com"], reply_to=[email])

            try:
             #   em.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?error")

    return render(request, "AppTienda/contacto.html", {"formulario": form})

def nuevo(request):
    cat = CategoriaProd.objects.all()
    if request.method=="POST":
        titulo=request.POST.get("titulo")
        descripcion=request.POST.get("descripcion")
        categoria=request.POST.get("categoria")
        imagen=request.POST.get("imagen")
        precio=request.POST.get("precio")

        bcat = CategoriaProd.objects.get(nombre=categoria)

        nuevo_prod=Producto(titulo=titulo,imagen=imagen,descripcion=descripcion,precio=precio,categoria=bcat)

        try:
            nuevo_prod.save()
            return redirect("/nuevo/?valido")
        except:
            return redirect("/nuevo/?error")        



    return render(request,"AppTienda/nuevo.html",{"categorias": cat})
