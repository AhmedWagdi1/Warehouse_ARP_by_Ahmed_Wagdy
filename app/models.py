# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models import CASCADE, DO_NOTHING
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Company(models.Model):
    company_name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.company_name


class Farm(models.Model):
    farm_name = models.CharField(max_length=250)
    farm_company = models.ForeignKey(Company, on_delete=CASCADE)

    def __unicode__(self):
        return self.farm_name

    def get_absolute_url(self):
        return reverse('farm_details', args=[str(self.id)])


class Job(models.Model):
    job_name = models.CharField(max_length=250)
    job_company = models.ForeignKey(Company, on_delete=CASCADE)

    def __unicode__(self):
        return self.job_name


class Worker(models.Model):
    worker_name = models.CharField(max_length=250)
    worker_phone = models.IntegerField()
    worker_id = models.IntegerField()
    worker_address = models.CharField(max_length=500)
    worker_job = models.ForeignKey(Job, on_delete=CASCADE)
    worker_farm = models.ForeignKey(Farm, on_delete=CASCADE)
    worker_salary = models.IntegerField()
    worker_work_date = models.DateField()
    worker_image = ProcessedImageField(upload_to='media',
                                       processors=[ResizeToFill(256, 256)],
                                       format='JPEG',
                                       options={'quality': 60},
                                       blank=True)
    worker_deleted = models.BooleanField(default=False)
    worker_end_time = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.worker_name

    def get_absolute_url(self):
        return reverse('worker_details', args=[str(self.id)])


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=85)

    def __unicode__(self):
        return self.supplier_name

    def get_absolute_url(self):
        return reverse('supplier_details', args=[str(self.id)])


class Client(models.Model):
    client_name = models.CharField(max_length=85)

    def __unicode__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('client_details', args=[str(self.id)])


class Product(models.Model):
    product_name = models.CharField(max_length=160)

    def __unicode__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_details', args=[str(self.id)])


class SellInvoice(models.Model):
    product = models.ForeignKey(Product, on_delete=DO_NOTHING)
    product2 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product2', default=1, blank=True, null=True)
    product3 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product3', blank=True, default=1, null=True)
    product4 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product4', blank=True, default=1, null=True)
    product5 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product5', blank=True, default=1, null=True)
    product6 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product6', blank=True, default=1, null=True)
    product7 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product7', blank=True, default=1, null=True)
    product8 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product8', blank=True, default=1, null=True)
    product9 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product9', blank=True, default=1, null=True)
    product10 = models.ForeignKey(Product, on_delete=DO_NOTHING, related_name='product10', blank=True, default=1, null=True)
    invoice_description = models.CharField(max_length=260, default='البيان')
    invoice_description2 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description3 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description4 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description5 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description6 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description7 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description8 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description9 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    invoice_description10 = models.CharField(max_length=260, default='البيان', blank=True, null=True)
    quantity = models.IntegerField(default=1)
    quantity2 = models.IntegerField(default=1, blank=True, null=True)
    quantity3 = models.IntegerField(default=1, blank=True, null=True)
    quantity4 = models.IntegerField(default=1, blank=True, null=True)
    quantity5 = models.IntegerField(default=1, blank=True, null=True)
    quantity6 = models.IntegerField(default=1, blank=True, null=True)
    quantity7 = models.IntegerField(default=1, blank=True, null=True)
    quantity8 = models.IntegerField(default=1, blank=True, null=True)
    quantity9 = models.IntegerField(default=1, blank=True, null=True)
    quantity10 = models.IntegerField(default=1, blank=True, null=True)
    price = models.IntegerField(default=1)
    price2 = models.IntegerField(default=1, blank=True, null=True)
    price3 = models.IntegerField(default=1, blank=True, null=True)
    price4 = models.IntegerField(default=1, blank=True, null=True)
    price5 = models.IntegerField(default=1, blank=True, null=True)
    price6 = models.IntegerField(default=1, blank=True, null=True)
    price7 = models.IntegerField(default=1, blank=True, null=True)
    price8 = models.IntegerField(default=1, blank=True, null=True)
    price9 = models.IntegerField(default=1, blank=True, null=True)
    price10 = models.IntegerField(default=1, blank=True, null=True)
    total = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=DO_NOTHING)
    date = models.DateField(auto_now=True)
    notes = models.TextField(max_length=1200, default='ملاحظات', blank=True)
    user = models.ForeignKey(User, on_delete=DO_NOTHING, default=1)
    source = models.CharField(max_length=180, default='الرئيسية')

    def __unicode__(self):
        return self.product


class Warehouse(models.Model):
    item_name = models.ForeignKey(Product, on_delete=CASCADE)
    item_quantity = models.IntegerField()

    def __unicode__(self):
        return self.item_name


class MainFinance(models.Model):
    balance = models.DecimalField(max_digits=8, decimal_places=2)


class MainFinanceMovement(models.Model):
    MODE_CHOICES = [('withdrawal', 'سحب'), ('deposite', 'إيداع')]
    mode = models.CharField(max_length=9, choices=MODE_CHOICES, default='1')
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=800)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
