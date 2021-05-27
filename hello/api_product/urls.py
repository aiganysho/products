
from django.urls import path, include
from rest_framework import routers
from api_product import views
from api_product.views import ProductView, OrderView


router = routers.DefaultRouter()
router.register(r'orders', views.OrderView )
router.register(r'products', views.ProductView)

app_name = 'api_prod'


urlpatterns = [
    path('', include(router.urls)),
    path('api-product/', include('rest_framework.urls', namespace='rest_framework')),
    # path('<int:pk>/', ProductView.as_view(), name='products'),

]





