from django.core.validators import MinValueValidator
from django.db import models

categories = [('food', 'food'), ('cell_phones', 'Cell_phones'), ('accessories', 'accessories'), ("other", "other")]



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    category = models.TextField(null=False, blank=False, choices=categories, default='other')
    remainder = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id}. {self.name}'
