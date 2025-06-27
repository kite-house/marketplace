from django.shortcuts import render
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from rest_framework import viewsets

# Create your views here.









# ======================== API ========================

class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', "put" ,'delete']

class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', "put" ,'delete']
    