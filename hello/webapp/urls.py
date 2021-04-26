from django.urls import path
from webapp.views import (
    ProductList,
    ProductDetailView,
    ProjectCreate,
    ProductUpdate,
    ProductDelete,
    ProductBasketCreate,
    ProductBasketView,
    ProductBasketDelete,
    CreateOrder,
    OrderView

)

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name="list"),
    path('<int:pk>/', ProductDetailView.as_view(), name="view"),
    path('product/add/', ProjectCreate.as_view(), name="add"),
    path('<int:pk>/update', ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/add/product/', ProductBasketCreate.as_view(), name='add_cart'),
    path('basket/', ProductBasketView.as_view(), name='view_cart'),
    path('<int:pk>/basket/delete/', ProductBasketDelete.as_view(), name='delete_cart'),
    path('basket/order/', CreateOrder.as_view(), name='order_cart'),
    path('order/products/', OrderView.as_view(), name='order_prod')

]
