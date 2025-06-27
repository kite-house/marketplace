from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория', unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    data_created = models.DateField(verbose_name= "Дата создание",auto_now_add=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(verbose_name= 'Скидка', blank=True, default=0, validators=[MaxValueValidator(100)])


    def __str__(self):
        return self.name

    def clean(self):
        if self.discount > 100:
            return ValueError('Данное значение не может быть больше 100%')

    @property
    def discount_in_percentages(self):
        return f'{self.discount}%'

    @property
    def amount(self):
        return self.price - ((self.price*self.discount)/100)