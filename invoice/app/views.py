from django.shortcuts import render
from rest_framework import viewsets
from .models import Invoice,Invoice_Detail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer



class InvoiceViewSet(viewsets.ModelViewSet):
    
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    
    queryset = Invoice_Detail.objects.all()
    serializer_class = InvoiceDetailSerializer