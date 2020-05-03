from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Certificate, Service
from .serializers import ProductSerializers,CertificateSerializers,ServiceSerializers

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers