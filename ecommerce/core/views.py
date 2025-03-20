from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
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
    permission_classes = [permissions.IsAuthenticated] # Solo usuarios logueados pueden ver los productos

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
    permission_classes = [permissions.IsAuthenticated] # Solo usuarios logueados pueden ver los articulos

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer 
    pagination_class = [permissions.IsAuthenticated] # Solo usuarios logueados pueden ver los comentarios


