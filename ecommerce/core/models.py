from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Usuario personalizado
class Usuario(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)  # El email será el identificador único
    es_admin = models.BooleanField(default=False)
    es_cliente = models.BooleanField(default=True)

    # Evitar conflicto de nombres en relaciones inversas
    groups = models.ManyToManyField(Group, related_name="usuario_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_set", blank=True)

# Categoría de productos y servicios
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

# Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

# Servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.TextField()  # Guardaremos las fechas disponibles como JSON
    
    def __str__(self):
        return self.nombre

# Pedido
class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    servicios = models.ManyToManyField(Servicio, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.username}"

# Carrito de Compras
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)
    servicios = models.ManyToManyField(Servicio, blank=True)
    
    def __str__(self):
        return f"Carrito de {self.usuario.username}"

# Blog y comentarios
class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username}"
