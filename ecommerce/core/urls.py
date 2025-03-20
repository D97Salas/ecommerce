from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProductoViewSet, PedidoViewSet, CarritoViewSet, ArticuloViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r"productos", ProductoViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"carritos", CarritoViewSet)
router.register(r"articulos", ArticuloViewSet)
router.register(r"comentarios", ComentarioViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
