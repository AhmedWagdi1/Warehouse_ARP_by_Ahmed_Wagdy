# -*- coding: utf-8 -*-
from django import forms

from app.models import Company, Farm, Job, Worker, Supplier, Client, Product, Warehouse, Daily, Type, Category


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
        fields = ['supplier_name', 'supplier_ID_number', 'supplier_mob_number']


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_ID_number', 'client_mobile_number']


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']


class WarehouseEntryForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['item_name', 'item_quantity']


class FundsTransfaerForm(forms.Form):
    farms = forms.ModelChoiceField(queryset=Farm.objects.all())
    amount = forms.IntegerField()








class AddDailyForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'البيان'
            }
        )
    )
    da2en = forms.IntegerField(required=False,
                               widget=forms.NumberInput(
                                   attrs={
                                       'style': 'max-width: 75px;',
                                       'placeholder': 'دائن',
                                       'value': 0,

                                   }
                               )
                               )
    maden = forms.IntegerField(required=False,
                               widget=forms.NumberInput(
                                   attrs={
                                       'style': 'max-width: 75px;',
                                       'placeholder': 'مدين',
                                       'value': 0,
                                   }
                               )
                               )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                          }
                                      )
                                      )

    class Meta:
        model = Daily
        fields = ['text', 'category', 'maden', 'da2en', 'farm']


class PickOstazForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'max-width': '650px;'
                                          }
                                      )
                                      )


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'type']


class AddNewDailyForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'width: 300px;'
            }
        )
    )
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False,
                                  widget=forms.Select(
                                      attrs={
                                          'style': 'width: 300px;'
                                      }
                                  )
                                  )
    maden = forms.IntegerField(required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width: 300px;',
                'value': '0',
            }
        )
    )
    da2en = forms.IntegerField(required=False,
        widget=forms.NumberInput(
            attrs={
                'style': 'width: 300px;',
                'value': '0',
            }
        )
    )

    farm = forms.ModelChoiceField(queryset=Farm.objects.all(),
                                  widget=forms.Select(
                                      attrs={
                                          'style': 'width: 300px;'
                                      }
                                  )
                                  )

    class Meta:
        model = Daily
        fields = ['text', 'maden', 'da2en', 'farm', 'category']

    def __init__(self, *args, **kwargs):
        myClient = kwargs.pop("typz")  # client is the parameter passed from views.py
        super(AddNewDailyForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(type=myClient),
                                                         widget=forms.Select(
                                                             attrs={
                                                                 'style': 'width: 300px;'
                                                             }
                                                         ))


class AddDailyOne(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all(),
                                  widget=forms.Select(
                                      attrs={
                                          'style': 'width: 300px;'
                                      }
                                  ))
