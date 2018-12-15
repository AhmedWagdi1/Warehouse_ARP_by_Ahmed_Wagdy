from django.contrib import admin
from app.models import Farm, Company, Job, Worker, Warehouse, Type, Category, Daily, Balance, Supplier, Client, \
    BuyInvoice, SellInvoice, Product, Talabat, Mezan, Account, Activation

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
admin.site.register(SellInvoice)
admin.site.register(Product)
admin.site.register(Talabat)
admin.site.register(Mezan)
admin.site.register(Account)
admin.site.register(Activation)
