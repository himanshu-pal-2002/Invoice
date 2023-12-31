from rest_framework.routers import DefaultRouter
from . views import InvoiceViewSet,InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice-details', InvoiceDetailViewSet)

urlpatterns = router.urls
