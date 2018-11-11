from django.core.management.base import BaseCommand
from app import models
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Company.objects.all().delete()
        models.Farm.objects.all().delete()
        models.Job.objects.all().delete()
        models.Worker.objects.all().delete()
        models.Supplier.objects.all().delete()
        models.Client.objects.all().delete()
        models.Product.objects.all().delete()
        models.Warehouse.objects.all().delete()
        models.Balance.objects.all().delete()
        models.Type.objects.all().delete()
        models.Category.objects.all().delete()
        models.Daily.objects.all().delete()
        models.BuyInvoice.objects.all().delete()
        models.SellInvoice.objects.all().delete()
        models.Talabat.objects.all().delete()
        models.Mezan.objects.all().delete()
        print('Databse is purged, Thank you !!')
