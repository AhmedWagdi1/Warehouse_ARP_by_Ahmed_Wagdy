# -*- coding: utf-8 -*-
from django import forms

from app.models import Company, Farm, Job, Worker, Supplier, Client, Product, Warehouse, SellInvoice, \
    MainFinanceMovement, BuyInvoice, FarmFinancemove, WorkingCosts, ManagmentCosts, Daily, Type, Category


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
        fields = ['supplier_name', 'supplier_ID_number']


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_ID_number']


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']


class WarehouseEntryForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['item_name', 'item_quantity']


class MainFinanceDepositForm(forms.ModelForm):
    class Meta:
        model = MainFinanceMovement
        fields = ['text', 'amount']


class MainFinanceWithdrawForm(forms.ModelForm):
    class Meta:
        model = MainFinanceMovement
        fields = ['text', 'amount']


class MainMangCosts(forms.Form):
    type = forms.ModelChoiceField(queryset=ManagmentCosts.objects.all())
    amount = forms.IntegerField()


class MainWorkCosts(forms.Form):
    type = forms.ModelChoiceField(queryset=WorkingCosts.objects.all())
    amount = forms.IntegerField()


class SellInvoiceForm(forms.ModelForm):
    product2 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product3 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product4 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product5 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product6 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product7 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product8 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product9 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product10 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    invoice_description2 = forms.CharField(required=False)
    invoice_description3 = forms.CharField(required=False)
    invoice_description4 = forms.CharField(required=False)
    invoice_description5 = forms.CharField(required=False)
    invoice_description6 = forms.CharField(required=False)
    invoice_description7 = forms.CharField(required=False)
    invoice_description8 = forms.CharField(required=False)
    invoice_description9 = forms.CharField(required=False)
    invoice_description10 = forms.CharField(required=False)
    quantity2 = forms.IntegerField(required=False)
    quantity3 = forms.IntegerField(required=False)
    quantity4 = forms.IntegerField(required=False)
    quantity5 = forms.IntegerField(required=False)
    quantity6 = forms.IntegerField(required=False)
    quantity7 = forms.IntegerField(required=False)
    quantity8 = forms.IntegerField(required=False)
    quantity9 = forms.IntegerField(required=False)
    quantity10 = forms.IntegerField(required=False)
    price2 = forms.IntegerField(required=False)
    price3 = forms.IntegerField(required=False)
    price4 = forms.IntegerField(required=False)
    price5 = forms.IntegerField(required=False)
    price6 = forms.IntegerField(required=False)
    price7 = forms.IntegerField(required=False)
    price8 = forms.IntegerField(required=False)
    price9 = forms.IntegerField(required=False)
    price10 = forms.IntegerField(required=False)
    total = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'readonly': 'true',
            }
        )
    )
    notes = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                }
                            )
                            )

    class Meta:
        model = SellInvoice
        fields = ['product', 'product2', 'product3', 'product4', 'product5', 'product6', 'product7', 'product8',
                  'product9', 'product10', 'invoice_description', 'invoice_description2', 'invoice_description3',
                  'invoice_description4', 'invoice_description5', 'invoice_description6', 'invoice_description7',
                  'invoice_description8', 'invoice_description9', 'invoice_description10', 'quantity', 'quantity2',
                  'quantity3', 'quantity4', 'quantity5', 'quantity6', 'quantity7', 'quantity8', 'quantity9',
                  'quantity10', 'price', 'price2', 'price3', 'price4', 'price5', 'price6', 'price7', 'price8', 'price9',
                  'price10', 'client', 'notes', 'total']


class BuyInvoiceForm(forms.ModelForm):
    product2 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product3 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product4 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product5 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product6 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product7 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product8 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product9 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    product10 = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    invoice_description2 = forms.CharField(required=False)
    invoice_description3 = forms.CharField(required=False)
    invoice_description4 = forms.CharField(required=False)
    invoice_description5 = forms.CharField(required=False)
    invoice_description6 = forms.CharField(required=False)
    invoice_description7 = forms.CharField(required=False)
    invoice_description8 = forms.CharField(required=False)
    invoice_description9 = forms.CharField(required=False)
    invoice_description10 = forms.CharField(required=False)
    quantity2 = forms.IntegerField(required=False)
    quantity3 = forms.IntegerField(required=False)
    quantity4 = forms.IntegerField(required=False)
    quantity5 = forms.IntegerField(required=False)
    quantity6 = forms.IntegerField(required=False)
    quantity7 = forms.IntegerField(required=False)
    quantity8 = forms.IntegerField(required=False)
    quantity9 = forms.IntegerField(required=False)
    quantity10 = forms.IntegerField(required=False)
    price2 = forms.IntegerField(required=False)
    price3 = forms.IntegerField(required=False)
    price4 = forms.IntegerField(required=False)
    price5 = forms.IntegerField(required=False)
    price6 = forms.IntegerField(required=False)
    price7 = forms.IntegerField(required=False)
    price8 = forms.IntegerField(required=False)
    price9 = forms.IntegerField(required=False)
    price10 = forms.IntegerField(required=False)
    total = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'readonly': 'true',
            }
        )
    )
    notes = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                }
                            )
                            )

    class Meta:
        model = BuyInvoice
        fields = ['product', 'product2', 'product3', 'product4', 'product5', 'product6', 'product7', 'product8',
                  'product9', 'product10', 'invoice_description', 'invoice_description2', 'invoice_description3',
                  'invoice_description4', 'invoice_description5', 'invoice_description6', 'invoice_description7',
                  'invoice_description8', 'invoice_description9', 'invoice_description10', 'quantity', 'quantity2',
                  'quantity3', 'quantity4', 'quantity5', 'quantity6', 'quantity7', 'quantity8', 'quantity9',
                  'quantity10', 'price', 'price2', 'price3', 'price4', 'price5', 'price6', 'price7', 'price8', 'price9',
                  'price10', 'client', 'notes', 'total']


# company = Company.objects.all()[0]


class FundsTransfaerForm(forms.Form):
    farms = forms.ModelChoiceField(queryset=Farm.objects.all())
    amount = forms.IntegerField()


class FarmFinancemoveForm(forms.ModelForm):
    class Meta:
        model = FarmFinancemove
        fields = ['text', 'amount']


class WorkingCostsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'إسم نوع المصروف',
            }
        )
    )

    class Meta:
        model = WorkingCosts
        fields = ['name']


class ManagementCostsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'إسم نوع المصروف',
            }
        )
    )

    class Meta:
        model = ManagmentCosts
        fields = ['name']


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
