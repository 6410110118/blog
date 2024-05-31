from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListCreate , ProductViewSet
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>', views.ProductDelete.as_view(), name='product-delete'),
]
