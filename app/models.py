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

    def __unicode__(self):
        return self.farm_name

    def get_absolute_url(self):
        return reverse('farm_details', args=[str(self.id)])


class Job(models.Model):
    job_name = models.CharField(max_length=250)

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
    supplier_ID_number = models.IntegerField()

    def __unicode__(self):
        return self.supplier_name

    def get_absolute_url(self):
        return reverse('supplier_details', args=[str(self.id)])


class Client(models.Model):
    client_name = models.CharField(max_length=85)
    client_ID_number = models.IntegerField()

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


class Warehouse(models.Model):
    item_name = models.ForeignKey(Product, on_delete=CASCADE)
    item_quantity = models.IntegerField()

    def __unicode__(self):
        return self.item_name
class Balance(models.Model):
    farm = models.ForeignKey(Farm, on_delete=CASCADE)
    balance = models.IntegerField()


class Type(models.Model):
    type_name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.type_name


class Category(models.Model):
    category_name = models.CharField(max_length=80)
    type = models.ForeignKey(Type, on_delete=CASCADE)

    def __unicode__(self):
        return self.category_name


    def get_absolute_url(self):
        return reverse('add_tawseef')


class Daily(models.Model):
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=80)
    total_da2en = models.IntegerField(default=0)
    total_maden = models.IntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=CASCADE)
    category = models.ForeignKey(Category , on_delete=CASCADE)
    maden = models.IntegerField(default=0)
    da2en = models.IntegerField(default=0)
    farm = models.ForeignKey(Farm, on_delete=DO_NOTHING)
