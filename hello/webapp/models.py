from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

categories = [('food', 'food'), ('cell_phones', 'Cell_phones'), ('accessories', 'accessories'), ("other", "other")]



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    category = models.TextField(null=False, blank=False, choices=categories, default='other')
    remainder = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])
    user = models.ManyToManyField(get_user_model(), related_name='products', null=False, blank=False, verbose_name='Пользователь')


    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        permissions = [
            ('have_user', 'есть пользователь')
        ]

    def __str__(self):
        return f'{self.id}. {self.name}'


class ProductInBasket(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        related_name='lists',
        null=False,
        blank=False
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'baskets'
        verbose_name = 'корзина'

    def __str__(self):
        return f'{self.id} {self.product} {self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Заказы',
        related_name='orders'
    )
    name_user = models.CharField(max_length=100, null=False, blank=False)
    telephone = models.CharField(null=False, blank=False, max_length=100)
    adress = models.CharField(null=False, blank=False, max_length=300)
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.id} {self.name_user} {self.telephone} '

    def sum_products(self):
        total = 0
        for order in self.order_product.all():
            total += order.quantity * order.product.price
        return total


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='product_order', on_delete=models.CASCADE)
    order = models.ForeignKey('webapp.Order', related_name='order_product', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "{} | {}".format(self.product, self.order)