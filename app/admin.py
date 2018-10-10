from django.contrib import admin
from app.models import Farm, Company, Job, Worker, Warehouse, MainFinance, MainFinanceMovement, SellInvoice, Balance, \
    BuyInvoice, FarmFinancemove

admin.site.register(Farm)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Worker)
admin.site.register(Warehouse)
admin.site.register(MainFinance)
admin.site.register(MainFinanceMovement)
admin.site.register(SellInvoice)
admin.site.register(Balance)
admin.site.register(BuyInvoice)
admin.site.register(FarmFinancemove)
