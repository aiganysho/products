from rest_framework import viewsets

from webapp.models import Product, Order
from api_product.serializer import ProductSerializer, OrderSerializer, OrderProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer