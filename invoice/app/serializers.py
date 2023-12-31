from rest_framework import serializers

from .models import Invoice,Invoice_Detail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_Detail
        fields = '__all__'
        
class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Invoice
        fields = '__all__'
        
        
        def create(self, validated_data):
            invoice_details_data = validated_data.pop('invoice_details', [])
            invoice = Invoice.objects.create(**validated_data)

            for invoice_detail_data in invoice_details_data:
                Invoice_Detail.objects.create(invoice=invoice, **invoice_detail_data)

            return invoice

        def update(self, instance, validated_data):
            invoice_details_data = validated_data.pop('invoice_details', [])

            instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
            instance.amount = validated_data.get('amount', instance.amount)
            instance.due_date = validated_data.get('due_date', instance.due_date)
            instance.save()

        # Update or create associated invoice_details
            instance.invoice_details.all().delete()
            for invoice_detail_data in invoice_details_data:
                Invoice_Detail.objects.create(invoice=instance, **invoice_detail_data)

            return instance