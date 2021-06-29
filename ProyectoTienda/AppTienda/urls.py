from django.urls import path
from AppTienda import views


app_name = 'Tienda'
urlpatterns = [
    path('', views.index, name="Index"),
    path('categorias/', views.categorias, name="Categorias"),
    path('categorias/<str:categoria>', views.categoria, name="b_categoria"),
    path('acerca/', views.acerca, name="Acerca"),
    path('contacto/', views.contacto, name="Contacto"),
    path('nuevo/', views.nuevo, name="Nuevo"),
    path('<int:prod_id>', views.ver_producto, name="VerProducto"),


]