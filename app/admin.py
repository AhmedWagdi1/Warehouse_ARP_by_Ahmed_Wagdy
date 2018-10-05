from django.contrib import admin
from app.models import Farm, Company, Job, Worker, Warehouse, MainFinance, MainFinanceMovement

admin.site.register(Farm)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Worker)
admin.site.register(Warehouse)
admin.site.register(MainFinance)
admin.site.register(MainFinanceMovement)