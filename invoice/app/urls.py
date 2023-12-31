# your_app/urls.py
from django.urls import path
from .views import InvoiceListCreateView, InvoiceDetailView, InvoiceDetailEntry

urlpatterns = [
    path('', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/', InvoiceDetailEntry.as_view(), name='invoice-entry'),
    # path('Invoice_Detail/', InvoiceDetailView.as_view(), name='Invoice_Detail'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]
