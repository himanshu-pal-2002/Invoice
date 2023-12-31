from django.db import models

# Create your models here.
class Invoice(models.Model):
    Date = models.DateField()
    Invoice_CustomerName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Invoice_CustomerName
    
class Invoice_Detail(models.Model):
    Invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    price = models.IntegerField()