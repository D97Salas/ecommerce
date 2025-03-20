from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Producto, Pedido, Carrito, Articulo, Comentario

Usuario = get_user_model()

# serializador de Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "username", "email", "first_name", "last_name"]

# serializador de producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

# serializador de pedido
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"

# serializador de carrito
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = "__all__"

# serializador de articulos
class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = "__all__"

# serializador de comentarios
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


