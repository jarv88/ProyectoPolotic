from django.db import models

# Create your models here.
class CategoriaProd(models.Model):
    nombre= models.CharField(max_length=20)

    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategoriasProd"
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    titulo= models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="AppTienda", null=True, blank=True)
    descripcion=models.CharField(max_length=150)
    precio = models.FloatField()
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    def __str__(self):
        return self.titulo

