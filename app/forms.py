# -*- coding: utf-8 -*-
from django import forms
import django_filters
from django_filters.widgets import RangeWidget

from app.models import Company, Farm, Job, Worker, Supplier, Client, Product, Warehouse, Daily, Type, Category, \
    BuyInvoice, SellInvoice


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


class AddBuyInvoice(forms.ModelForm):
    class Meta:
        model = BuyInvoice
        fields = ['supplier', 'product', 'quantity', 'price', 'category', 'farm']


class AddSellInvoice(forms.ModelForm):
    class Meta:
        model = SellInvoice
        fields = ['client', 'product', 'quantity', 'price', 'category', 'farm']


class FarmReportForm(forms.Form):
    farm = forms.ModelChoiceField(queryset=Farm.objects.all(),
                                  widget=forms.Select()
                                  )


class SellInvoiceFilterForm(django_filters.FilterSet):
    date_range = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': '2018/10/12'}))

    # date_range = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': '2018/10/12','type':'date'}))

    class Meta:
        model = SellInvoice
        fields = ['client', 'product', 'category', 'farm', ]


class BuyInvoiceFilterForm(django_filters.FilterSet):
    # date__range = django_filters.DateFromToRangeFilter(field_name='date', lookup_expr='month__gt')
    date_range = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': '2018/10/12'}))

    class Meta:
        model = BuyInvoice
        fields = ['supplier', 'product', 'category', 'farm', ]


class NewDailyForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'البيان',
                   'class': 'form-control',
                   }
        )
    )

    maden_from_type = forms.ModelChoiceField(required=False, queryset=Type.objects.all(),
                                             widget=forms.Select(
                                             )
                                             )
    da2en_from_type = forms.ModelChoiceField(required=False, queryset=Type.objects.all(),
                                             widget=forms.Select(
                                             )
                                             )
    maden_from_cat = forms.ModelChoiceField(required=False, queryset=Category.objects.all(),
                                            widget=forms.Select(

                                            ))
    da2en_from_cat = forms.ModelChoiceField(required=False, queryset=Category.objects.all(),
                                            widget=forms.Select(

                                            ))

    class Meta:
        model = Daily
        fields = ['text', 'maden', 'maden_from_type', 'maden_from_cat', 'da2en', 'da2en_from_type', 'da2en_from_cat',
                  'farm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['maden_from_cat'].queryset = Category.objects.none()
        self.fields['da2en_from_cat'].queryset = Category.objects.none()

        if 'maden_from_type' in self.data:
            try:
                country_id = int(self.data.get('maden_from_type'))
                self.fields['maden_from_cat'].queryset = Category.objects.filter(type=country_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['maden_from_cat'].queryset = self.instance.type.city_set
        if 'da2en_from_type' in self.data:
            try:
                country_id = int(self.data.get('da2en_from_type'))
                self.fields['da2en_from_cat'].queryset = Category.objects.filter(type=country_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['da2en_from_cat'].queryset = self.instance.type.city_set
