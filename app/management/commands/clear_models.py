from django.core.management.base import BaseCommand
from app import models
import time
from django.contrib.auth.models import User
from django.core.management import call_command

class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')
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
        models.Account.objects.all().delete()
        User.objects.all().delete()
        admin_username = 'admin'
        admin_password = 'admin'
        new_admin = User(username=admin_username, is_superuser=True, is_staff=True)
        new_admin.set_password(admin_password)
        new_admin.save()
        admin_account = models.Account(user=new_admin, role='المديرين')
        admin_account.save()
        default_company = models.Company(company_name= 'Demo Version')
        default_company.save()
        print('Databse is purged, Thank you !!')
