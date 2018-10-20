from django.contrib import admin
from app.models import Farm, Company, Job, Worker, Warehouse, Type, Category, Daily, Balance, Supplier, Client, \
    BuyInvoice

admin.site.register(Farm)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Worker)
admin.site.register(Warehouse)
admin.site.register(Balance)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Daily)
admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(BuyInvoice)
