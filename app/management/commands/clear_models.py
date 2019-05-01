from django.core.management.base import BaseCommand
from app import models
import time
from django.contrib.auth.models import User
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')
        call_command('flush', '--noinput')
        print('Deleted Database')
        admin_username = 'admin'
        admin_password = 'admin'
        new_admin = User(username=admin_username, is_superuser=True, is_staff=True)
        new_admin.set_password(admin_password)
        new_admin.save()
        admin_account = models.Account(user=new_admin, role='المديرين')
        admin_account.save()
        print('created account // username: admin -- password: admin')
        default_company = models.Company(company_name='Zoom Print')
        default_company.save()
        print('Company named ' + default_company.company_name + ' Created.!')
