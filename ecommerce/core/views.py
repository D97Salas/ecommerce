from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from google.auth.transport import requests
from google.oauth2 import id_token
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Producto, Pedido, Carrito, Articulo, Comentario
from .serializers import (
    ProductoSerializer,
    PedidoSerializer,
    CarritoSerializer,
    ArticuloSerializer,
    ComentarioSerializer,
)


# Vistas para los modelos
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny] # Cualquiera puede ver los productos
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated] # Solo usuarios logueados pueden ver los pedidos

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated] # Solo usuarios logueados pueden ver los carritos

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.AllowAny] # cualquiera puede ver los articulos

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer 
    pagination_class = [permissions.IsAuthenticated] # Solo usuarios logueados pueden ver los comentarios


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def obtener_usuario(request):
    usuario = request.user
    data = {
        "id": usuario.id,
        "email": usuario.email,
        "es_admin": usuario.es_admin,
        "es_cliente": usuario.es_cliente,
    }
    return Response(data)

@api_view(["POST"])
def google_login(request):
    token = request.data.get("token")
    try:
        # Verifica el token de Google
        info = id_token.verify_oauth2_token(token, requests.Request(), settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY)

        # Obtener o crear el usuario
        Usuario = get_user_model()
        usuario, creado = Usuario.objects.get_or_create(email=info["email"], defaults={"username": info["email"]})

        # Generar token JWT
        refresh = RefreshToken.for_user(usuario)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)