from django.test import TestCase
from .models import Product, Category 
from django.db.utils import IntegrityError

# Create your tests here.

class ProductTestClass(TestCase):

    def setUp(self):
        Category.objects.bulk_create([
            Category(name = 'Электроника'), 
            Category(name = 'Химия'), 
            Category(name = 'Игрушки')
        ])

    def test_correct_amount(self):
        Product.objects.create(
            name = 'Компьютер',
            description = 'Очень вкусный и красивый',
            category = Category.objects.get(name = 'Электроника'),
            price = 2500,
            discount = 50
        )

        product = Product.objects.get(name = 'Компьютер')
        self.assertEqual(product.amount, 1250, 'incorrect invoice amount')

    def test_percentages_min(self):
        # checking discount < 0

        try:
            Product.objects.create(
                name = 'Доместос',
                category = Category.objects.get(name = 'Химия'),
                price = 2500,
                discount = -100
            )
        except IntegrityError:
            pass

        else:
            raise AssertionError('The percentage value may be less than 0')

