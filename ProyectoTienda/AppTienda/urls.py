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
    path('buscar/', views.buscar, name="Buscar"),
    path('registro/', views.registrarse, name="registrarse"),
    path('logout/', views.logout, name="logout"),
    path('<int:prod_id>', views.ver_producto, name="VerProducto"),
    path('<int:prod_id>/editar/', views.editar_producto, name="EditarProducto"),
    #path('<int:prod_id>/editar/update', views.update_editar_producto, name="UpdateEditarProducto"),
    path('agregar/<int:prod_id>', views.agregar_producto, name="AgregarProducto"),
    path('carro/', views.ver_carro, name="VerCarro"),
    path('carro/limpiar', views.limpiar_carro, name="LimpiarCarro"),
    path('carro/restar/<int:prod_id>', views.restar_producto, name="RestarCarro"),
    path('eliminar/<int:prod_id>', views.eliminar_producto, name="EliminarProducto"),


]