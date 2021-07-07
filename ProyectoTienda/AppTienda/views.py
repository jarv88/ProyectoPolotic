from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Producto, CategoriaProd
from .forms import ContactForm, ImagenUploadForm,RegistroForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import logout
from .carro import Carro
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
def index(request):
    productos=Producto.objects.all()
    return render(request,"AppTienda/index.html",{ "productos": productos })

def categorias(request):
    cat = CategoriaProd.objects.all()
    return render(request, "AppTienda/categorias.html", {"categorias": cat})

def categoria(request,categoria):
    cat = CategoriaProd.objects.get(nombre=categoria)
    productos= Producto.objects.filter(categoria=cat.id)
    
    #cat = CategoriaProd.objects.all()
    return render(request, "AppTienda/categoria.html", {"productos": productos, "categoria": cat})

def acerca(request):
    return render(request, "AppTienda/acerca.html",)

def buscar(request):
    if request.method == "POST":
        texto = request.POST.get("buscar")
        productos=Producto.objects.filter(titulo__contains=texto)
        return render(request,"AppTienda/buscar.html",{"productos":productos})


def contacto(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")

            #send_mail(nombre,contenido,) #otra forma
            em = EmailMessage("Mensaje desde App",
                              "El usuario {}, email: {}, escribe: \n\n {}".format(nombre, email, mensaje),
                              "", [settings.EMAIL_HOST_USER], reply_to=[email])

            try:
                em.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?error")

    return render(request, "AppTienda/contacto.html", {"formulario": form})

@permission_required('Tienda.add_producto')
def nuevo(request):
    cat = CategoriaProd.objects.all()
    #Incluido para poder tener upload_to al momento de guardar la imagen
    #Se puede mejorar
    form = ImagenUploadForm(request.POST, request.FILES)
    if form.is_valid():
        img=form.cleaned_data['imagen']
    ########################################################
    ########################################################
    if request.method=="POST":

    
        titulo=request.POST.get("titulo")
        descripcion=request.POST.get("descripcion")
        categoria=request.POST.get("categoria")
        imagen=img  #request.POST.get("imagen")
        precio=request.POST.get("precio")

        bcat = CategoriaProd.objects.get(nombre=categoria)

        nuevo_prod=Producto(titulo=titulo,imagen=imagen,descripcion=descripcion,precio=precio,categoria=bcat)

        try:
            nuevo_prod.save()
            return redirect("/nuevo/?valido")
        except:
            return redirect("/nuevo/?error")        



    return render(request,"AppTienda/nuevo.html",{"categorias": cat})


def ver_producto(request,prod_id):
    
    producto= Producto.objects.get(id=prod_id)
    
    #cat = CategoriaProd.objects.all()
    return render(request, "AppTienda/ver_producto.html", {"producto": producto,})

@permission_required('Tienda.change_producto')
@permission_required('Tienda.delete_producto')
def editar_producto(request,prod_id):
    cat = CategoriaProd.objects.all()
    producto= Producto.objects.get(id=prod_id)
    list_cat=[]
    for c in cat:
        list_cat.append(c)

    if request.method=="POST":
        form = ImagenUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img=form.cleaned_data['imagen']

        titulo=request.POST.get("titulo")
        descripcion=request.POST.get("descripcion")
        categoria=request.POST.get("categoria")
        imagen=img  #request.POST.get("imagen")
        precio=request.POST.get("precio")

        bcat = CategoriaProd.objects.get(nombre=categoria)
        update_prod=Producto.objects.get(id=request.POST.get("id"))
        update_prod.titulo=titulo
        update_prod.descripcion=descripcion
        update_prod.categoria=bcat
        update_prod.precio=precio
        update_prod.imagen=imagen

        #nuevo_prod=Producto(titulo=titulo,imagen=imagen,descripcion=descripcion,precio=precio,categoria=bcat)

        try:
            id=request.POST.get("id")
            update_prod.save()
            #return HttpResponseRedirect(reverse("Tienda:EditarProducto", args=(producto.id,)))
            return redirect(f"/{id}/editar/?valido")
        except:
            return redirect(f"/{id}/editar/?error")
    return render(request, "AppTienda/editar_producto.html", {"producto": producto,"categorias": list_cat})

def eliminar_producto(request,prod_id):
    producto= Producto.objects.get(id=prod_id)
    try:
        producto.delete()
        return redirect("/")
    except:
        print("error")
        return redirect("/")
      







def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():

            try:
                form.save()    
                return redirect("/accounts/login/?valido") 
            except:
                return redirect("/accounts/login/?error")     
            #return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
        })

def logout(request):
    logout(request)
    return redirect("/accounts/login/")

######################################
###Vistas para el carrito de compra###
######################################
@login_required
def agregar_producto(request,prod_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=prod_id)
    carro.agregar(producto=producto)
    #print(carro)
    #print(producto.precio)

    return redirect("/")
"""
def eliminar_producto(request,prod_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=prod_id)
    carro.eliminar(producto=producto)

    return redirect("tienda")
"""
def restar_producto(request,prod_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=prod_id)
    carro.restar_producto(producto=producto)
    return redirect("/carro")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("/")

    

def ver_carro(request):
    carro= request.session.get("carro")
    #print(carro)
    return render(request, "AppTienda/ver_carro.html", {"carro": carro,})

