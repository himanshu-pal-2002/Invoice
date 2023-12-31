from rest_framework import generics
from .models import Invoice,Invoice_Detail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer



class InvoiceListCreateView(generics.ListCreateAPIView):
    
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Invoice_Detail.objects.all()
    serializer_class = InvoiceDetailSerializer