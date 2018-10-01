# -*- coding: utf-8 -*-
from django import forms

from app.models import Company, Farm, Job, Worker, Supplier, Client, Product, Warehouse


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name']


class AddFarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name']


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_name']


class AddWorkerForm(forms.ModelForm):
    worker_work_date = forms.DateField(widget=forms.DateInput(attrs=
    {
        'type': 'date'
    }))

    class Meta:
        model = Worker
        fields = ['worker_name', 'worker_phone', 'worker_id', 'worker_address', 'worker_job', 'worker_farm',
                  'worker_salary', 'worker_work_date']


class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name']


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name']


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']


class WarehouseEntryForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['item_name', 'item_quantity']
