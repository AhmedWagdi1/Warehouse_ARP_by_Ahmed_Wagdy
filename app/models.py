# -*- coding: utf-8 -*-
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


class Client(models.Model):
    client_name = models.CharField(max_length=85)

    def __unicode__(self):
        return self.client_name


class InvoiceType(models.Model):
    invoice_type = models.CharField(max_length=85)

    def __unicode__(self):
        return self.invoice_type


class Product(models.Model):
    product_name = models.CharField(max_length=160)

    def __unicode__(self):
        return self.product_name


class Invoice(models.Model):
    product = models.ForeignKey(Product, on_delete=DO_NOTHING)
    product_description = models.CharField(max_length=260)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.product


class Warehouse(models.Model):
    item_name = models.CharField(max_length=160)
    item_quantity = models.IntegerField()

    def __unicode__(self):
        return self.item_name
