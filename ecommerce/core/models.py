from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models

# Manager personalizado para manejar usuarios sin username
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

# Modelo de usuario personalizado
class Usuario(AbstractUser):
    username = None  # Eliminamos el username
    email = models.EmailField(unique=True)  # Email como identificador único
    es_admin = models.BooleanField(default=False)
    es_cliente = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name="usuario_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_set", blank=True)

    USERNAME_FIELD = "email"  # Usamos email para autenticación
    REQUIRED_FIELDS = []  # No necesitamos username

    objects = UsuarioManager()  # Asignamos nuestro UserManager personalizado

    def __str__(self):
        return self.email

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
