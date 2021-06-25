from django.urls import path
from AppTienda import views


app_name = 'Tienda'
urlpatterns = [
    path('', views.index, name="Index"),
    path('categorias/', views.categorias, name="Categorias"),
    path('acerca/', views.acerca, name="Acerca"),
    path('contacto/', views.contacto, name="Contacto"),
    path('', views.nuevo, name="Nuevo"),


]