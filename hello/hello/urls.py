"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
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
    CreateOrder
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductList.as_view(), name="list-product"),
    path('<int:pk>/', ProductDetailView.as_view(), name="view-product"),
    path('product/add/', ProjectCreate.as_view(), name="add-product"),
    path('<int:pk>/update', ProductUpdate.as_view(), name='update-product'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete-product'),
    path('<int:pk>/add/product/', ProductBasketCreate.as_view(), name='add_cart'),
    path('basket/', ProductBasketView.as_view(), name='view_cart'),
    path('<int:pk>/basket/delete/', ProductBasketDelete.as_view(), name='delete_cart'),
    path('basket/order/', CreateOrder.as_view(), name='order_cart')

]


