# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic.edit import UpdateView
from app.forms import AddCompanyForm, AddFarmForm, AddJobForm, AddWorkerForm, AddSupplierForm, AddClientForm, \
    AddProductForm, WarehouseEntryForm, FundsTransfaerForm, AddDailyForm, PickOstazForm, AddCategoryForm, \
    AddNewDailyForm, AddDailyOne, AddBuyInvoice, AddSellInvoice, FarmReportForm
from app.models import Company, Farm, Job, Worker, Supplier, Client, Warehouse, Product, Balance, Daily, Type, Category, \
    SellInvoice, BuyInvoice
from datetime import date, datetime


def index(request):
    return render(request, 'app/add_farm.html')


@login_required
def workers(request):
    all_workers = Worker.objects.filter(worker_deleted=False)
    context = {
        'all_workers': all_workers,
    }
    return render(request, 'app/workers.html', context)


def nocomp(request):
    return render(request, 'app/nocomp.html')


@login_required
def add_company(request):
    add_company_form = AddCompanyForm(request.POST)
    if request.method == 'POST':
        if add_company_form.is_valid():
            add_company_form.save()
            return redirect('index')
    else:
        add_company_form = AddCompanyForm()

    context = {
        'add_company_form': add_company_form,
    }

    return render(request, 'app/add_company.html', context)


@login_required
def add_farm(request):
    add_farm_form = AddFarmForm(request.POST)
    if request.method == 'POST':
        if add_farm_form.is_valid():
            ad_farm = add_farm_form.save(commit=False)
            ad_farm.save()
            add_balance = Balance(farm=ad_farm, balance=0)
            add_balance.save()
            return redirect('index')
    else:
        add_farm_form = AddFarmForm()

    context = {
        'add_farm_form': add_farm_form,
    }
    return render(request, 'app/add_farm.html', context)


@login_required
def farm_details(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    farm_workers = Worker.objects.filter(worker_farm=current_farm, worker_deleted=False)
    context = {
        'current_farm': current_farm,
        'farm_workers': farm_workers,
    }
    return render(request, 'app/farm_details.html', context)


@login_required
def farm_delete(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    current_farm.delete()
    return redirect('index')


class FarmUpdate(UpdateView):
    model = Farm
    fields = ['farm_name']
    template_name_suffix = '_update_form'


@login_required
def workers_add(request):
    add_worker_form = AddWorkerForm(request.POST)
    if request.method == 'POST':
        if add_worker_form.is_valid():
            add_worker_form.save()
            return redirect('workers')
    else:
        add_worker_form = AddWorkerForm()
    context = {
        'add_worker_form': add_worker_form,
    }

    return render(request, 'app/workers_add.html', context)


@login_required
def jobs_add(request):
    add_job_form = AddJobForm(request.POST)
    all_jobs = Job.objects.all()
    if request.method == 'POST':
        if add_job_form.is_valid():
            ad_job = add_job_form.save(commit=False)
            ad_job.save()
            return redirect('jobs_add')
    else:
        add_job_form = AddJobForm()

    context = {
        'add_job_form': add_job_form,
        'all_jobs': all_jobs,
    }

    return render(request, 'app/jobs_add.html', context)


@login_required
def job_delete(request, pk):
    current_job = get_object_or_404(Job, pk=pk)
    current_job.delete()
    return redirect('jobs_add')


class JobUpdate(UpdateView):
    model = Job
    fields = ['job_name']
    template_name_suffix = '_update_form'


@login_required
def worker_details(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    context = {
        'current_worker': current_worker,
    }
    return render(request, 'app/worker_details.html', context)


@login_required
def worker_delete(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    current_worker.delete()
    return redirect('workers')


class WorkerUpdate(UpdateView):
    model = Worker
    fields = ['worker_name', 'worker_phone', 'worker_id', 'worker_address', 'worker_job', 'worker_farm',
              'worker_salary', 'worker_work_date', 'worker_image']
    template_name_suffix = '_update_form'


@login_required
def worker_archive(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    current_worker.worker_end_time = date.today()
    current_worker.worker_deleted = True
    current_worker.save()
    return redirect('workers')


@login_required
def old_workers(request):
    old_worker = Worker.objects.filter(worker_deleted=True)
    context = {
        'old_worker': old_worker,
    }
    return render(request, 'app/old_workers.html', context)


@login_required
def supplier(request):
    all_supply = Supplier.objects.all()
    context = {
        'all_supply': all_supply,
    }
    return render(request, 'app/supplier.html', context)


@login_required
def supplier_add(request):
    add_supplier_form = AddSupplierForm(request.POST)
    if request.method == 'POST':
        if add_supplier_form.is_valid():
            add_supplier_form.save()
            return redirect('supplier')
    else:
        add_supplier_form = AddSupplierForm()
    context = {
        'add_supplier_form': add_supplier_form,
    }
    return render(request, 'app/add_supplier.html', context)


@login_required
def clients(request):
    all_clients = Client.objects.all()
    context = {
        'all_clients': all_clients,
    }
    return render(request, 'app/clients.html', context)


@login_required
def clients_add(request):
    add_client_form = AddClientForm(request.POST)
    if request.method == 'POST':
        if add_client_form.is_valid():
            add_client_form.save()
            return redirect('clients')
    else:
        add_client_form = AddClientForm()
    context = {
        'add_client_form': add_client_form,
    }
    return render(request, 'app/clients_add.html', context)


@login_required
def supplier_delete(request, pk):
    current_supply = get_object_or_404(Supplier, pk=pk)
    current_supply.delete()
    return redirect('supplier')


class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['supplier_name', 'supplier_ID_number']
    template_name_suffix = '_update_form'


@login_required
def supplier_details(request, pk):
    current_supply = get_object_or_404(Supplier, pk=pk)
    context = {
        'current_supply': current_supply,
    }
    return render(request, 'app/supplier_details.html', context)


@login_required
def client_details(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    context = {
        'current_client': current_client,
    }
    return render(request, 'app/client_details.html', context)


@login_required
def client_delete(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    current_client.delete()
    return redirect('clients')


class ClientUpdate(UpdateView):
    model = Client
    fields = ['client_name', 'client_ID_number']
    template_name_suffix = '_update_form'


@login_required
def warehouse(request):
    all_warehouse = Warehouse.objects.all()
    context = {
        'all_warehouse': all_warehouse,
    }
    return render(request, 'app/warehouse.html', context)


@login_required
def product(request):
    all_products = Product.objects.all()
    context = {
        'all_products': all_products,
    }
    return render(request, 'app/product.html', context)


@login_required
def product_add(request):
    add_product_form = AddProductForm(request.POST)
    if request.method == 'POST':
        if add_product_form.is_valid():
            add_product_form.save()
            return redirect('product')
    else:
        add_product_form = AddProductForm()
    context = {
        'add_product_form': add_product_form,
    }
    return render(request, 'app/product_add.html', context)


@login_required
def product_details(request, pk):
    current_product = get_object_or_404(Product, pk=pk)
    context = {
        'current_product': current_product,
    }
    return render(request, 'app/product_details.html', context)


@login_required
def product_delete(request, pk):
    current_product = get_object_or_404(Product, pk=pk)
    current_product.delete()
    return redirect('product')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['product_name']
    template_name_suffix = '_update_form'


@login_required
def warehouse_entry(request):
    warehouse_entry_form = WarehouseEntryForm(request.POST)
    if request.method == 'POST':
        if warehouse_entry_form.is_valid():
            ada_entry = warehouse_entry_form.save(commit=False)
            current = Warehouse.objects.filter(item_name=ada_entry.item_name)
            if current:
                current1 = current[0]
                current2 = current1.item_quantity
                current3 = current2 + ada_entry.item_quantity
                current1.item_quantity = current3
                current1.save()
                return redirect('warehouse')
            else:
                ada_entry.save()
                return redirect('warehouse')
    else:
        warehouse_entry_form = WarehouseEntryForm()
    context = {
        'warehouse_entry_form': warehouse_entry_form,
    }
    return render(request, 'app/warehouse_entry.html', context)


@login_required
def warehouse_out(request, pk):
    current_item = get_object_or_404(Warehouse, pk=pk)
    quantity = request.POST.get('out_number')
    current = current_item.item_quantity
    if request.method == 'POST':
        new = int(current) - int(quantity)
        current_item.item_quantity = new
        current_item.save()
        return redirect('warehouse')
    context = {
        'current_item': current_item,
        'current': current,
    }
    return render(request, 'app/item_out.html', context)


def finance_daily(request):
    add_daily_form = AddDailyForm(request.POST)
    all_daily = Daily.objects.all().order_by('-date')
    all_da2en = []
    for item in all_daily:
        all_da2en.append(item.total_da2en)
    final_all_da2en = sum(all_da2en)
    if request.method == 'POST':
        if add_daily_form.is_valid():
            form = add_daily_form.save(commit=False)
            form.total_da2en = form.da2en
            form.total_maden = form.maden
            form.type = form.category.type
            form.save()
            return redirect('finance_daily')
    else:
        add_daily_form = AddDailyForm()
    context = {
        'add_daily_form': add_daily_form,
        'all_daily': all_daily,
        'final_all_da2en': final_all_da2en,
    }
    return render(request, 'app/finance_daily.html', context)


def ostaz(request):
    pick_ostaz_form = PickOstazForm(request.POST)
    if request.method == 'POST':
        if pick_ostaz_form.is_valid():
            current_type = pick_ostaz_form.cleaned_data['category']
            return redirect('ostaz_details', pk=current_type.pk)
    else:
        pick_ostaz_form = PickOstazForm()
    context = {
        'pick_ostaz_form': pick_ostaz_form,
    }
    return render(request, 'ostaz.html', context)


def ostaz_details(request, pk):
    current_category = get_object_or_404(Category, pk=pk)
    pick_ostaz_form = PickOstazForm(request.POST)
    all_current = Daily.objects.filter(category=current_category)
    jan_maden = []
    feb_maden = []
    march_maden = []
    april_maden = []
    may_maden = []
    june_maden = []
    july_maden = []
    aug_maden = []
    sep_maden = []
    oct_maden = []
    nov_maden = []
    dec_maden = []
    jan_da2en = []
    feb_da2en = []
    march_da2en = []
    april_da2en = []
    may_da2en = []
    june_da2en = []
    july_da2en = []
    aug_da2en = []
    sep_da2en = []
    oct_da2en = []
    nov_da2en = []
    dec_da2en = []
    for item in all_current:
        if item.date.month == 1:
            jan_maden.append(item.total_maden)
            jan_da2en.append(item.total_da2en)
    final_1_maden = sum(jan_maden)
    final_1_da2en = sum(jan_da2en)
    for item in all_current:
        if item.date.month == 2:
            feb_maden.append(item.total_maden)
            feb_da2en.append(item.total_da2en)
    final_2_maden = sum(feb_maden)
    final_2_da2en = sum(feb_da2en)
    for item in all_current:
        if item.date.month == 3:
            march_maden.append(item.total_maden)
            march_da2en.append(item.total_da2en)
    final_3_maden = sum(march_maden)
    final_3_da2en = sum(march_da2en)
    for item in all_current:
        if item.date.month == 4:
            april_maden.append(item.total_maden)
            april_da2en.append(item.total_da2en)
    final_4_maden = sum(april_maden)
    final_4_da2en = sum(april_da2en)
    for item in all_current:
        if item.date.month == 5:
            may_maden.append(item.total_maden)
            may_da2en.append(item.total_da2en)
    final_5_maden = sum(may_maden)
    final_5_da2en = sum(may_da2en)
    for item in all_current:
        if item.date.month == 6:
            june_maden.append(item.total_maden)
            june_da2en.append(item.total_da2en)
    final_6_maden = sum(june_maden)
    final_6_da2en = sum(june_da2en)
    for item in all_current:
        if item.date.month == 7:
            july_maden.append(item.total_maden)
            july_da2en.append(item.total_da2en)
    final_7_maden = sum(july_maden)
    final_7_da2en = sum(july_da2en)
    for item in all_current:
        if item.date.month == 8:
            aug_maden.append(item.total_maden)
            aug_da2en.append(item.total_da2en)
    final_8_maden = sum(aug_maden)
    final_8_da2en = sum(aug_da2en)
    for item in all_current:
        if item.date.month == 9:
            sep_maden.append(item.total_maden)
            sep_da2en.append(item.total_da2en)
    final_9_maden = sum(sep_maden)
    final_9_da2en = sum(sep_da2en)
    for item in all_current:
        if item.date.month == 10:
            oct_maden.append(item.total_maden)
            oct_da2en.append(item.total_da2en)
    final_10_maden = sum(oct_maden)
    final_10_da2en = sum(oct_da2en)
    for item in all_current:
        if item.date.month == 11:
            nov_maden.append(item.total_maden)
            nov_da2en.append(item.total_da2en)
    final_11_maden = sum(nov_maden)
    final_11_da2en = sum(nov_da2en)
    for item in all_current:
        if item.date.month == 12:
            dec_maden.append(item.total_maden)
            dec_da2en.append(item.total_da2en)
    final_12_maden = sum(dec_maden)
    final_12_da2en = sum(dec_da2en)
    if request.method == 'POST':
        if pick_ostaz_form.is_valid():
            current_category = pick_ostaz_form.cleaned_data['category']
            return redirect('ostaz_details', pk=current_category.pk)
    else:
        pick_ostaz_form = PickOstazForm()
    context = {
        'current_category': current_category,
        'pick_ostaz_form': pick_ostaz_form,
        'all_current': all_current,
        'final_1_maden': final_1_maden,
        'final_2_maden': final_2_maden,
        'final_3_maden': final_3_maden,
        'final_4_maden': final_4_maden,
        'final_5_maden': final_5_maden,
        'final_6_maden': final_6_maden,
        'final_7_maden': final_7_maden,
        'final_8_maden': final_8_maden,
        'final_9_maden': final_9_maden,
        'final_10_maden': final_10_maden,
        'final_11_maden': final_11_maden,
        'final_12_maden': final_12_maden,
        'final_1_da2en': final_1_da2en,
        'final_2_da2en': final_2_da2en,
        'final_3_da2en': final_3_da2en,
        'final_4_da2en': final_4_da2en,
        'final_5_da2en': final_5_da2en,
        'final_6_da2en': final_6_da2en,
        'final_7_da2en': final_7_da2en,
        'final_8_da2en': final_8_da2en,
        'final_9_da2en': final_9_da2en,
        'final_10_da2en': final_10_da2en,
        'final_11_da2en': final_11_da2en,
        'final_12_da2en': final_12_da2en,
    }
    return render(request, 'ostaz_details.html', context)


def mezan(request):
    all_daily = Daily.objects.values('category__category_name').annotate(all_maden=Sum('total_maden')).annotate(
        all_da2en=Sum('total_da2en'))
    context = {
        'all_daily': all_daily,
    }
    return render(request, 'mezan.html', context)


def add_tawseef(request):
    all_cats = Category.objects.all()
    add_category_form = AddCategoryForm(request.POST)
    if request.method == 'POST':
        if add_category_form.is_valid():
            add_category_form.save()
            return redirect('add_tawseef')
    else:
        add_category_form = AddCategoryForm()
    context = {
        'all_cats': all_cats,
        'add_category_form': add_category_form,
    }
    return render(request, 'add_tawseef.html', context)


def delete_tawseef(request, pk):
    current_tawseef = get_object_or_404(Category, pk=pk)
    current_tawseef.delete()
    return redirect('add_tawseef')


class TawseefUpdate(UpdateView):
    model = Category
    fields = ['category_name', 'type']
    template_name_suffix = '_update_form'


def add_new_daily(request, pk):
    current_type = get_object_or_404(Type, pk=pk)
    add_new_daily_form = AddNewDailyForm(request.POST, typz=current_type)
    if request.method == 'POST':
        if add_new_daily_form.is_valid():
            form = add_new_daily_form.save(commit=False)
            form.total_da2en = form.da2en
            form.total_maden = form.maden
            form.type = current_type
            form.save()
            current_farm = form.farm
            current_balance = Balance.objects.get(farm=current_farm)
            if form.maden != 0:
                added_balance = form.maden
                new_balance = int(current_balance.balance) - int(added_balance)
                current_balance.balance = new_balance
                current_balance.save()
            if form.da2en != 0:
                added_balance = form.da2en
                new_balance = int(current_balance.balance) + int(added_balance)
                current_balance.balance = new_balance
                current_balance.save()
            return redirect('finance_daily')
    else:
        add_new_daily_form = AddNewDailyForm(typz=current_type)
    context = {
        'add_new_daily_form': add_new_daily_form,
        'current_type': current_type,
    }
    return render(request, 'add_new_daily.html', context)


def add_daily_one(request):
    add_daily_one_form = AddDailyOne(request.POST)
    if request.method == 'POST':
        if add_daily_one_form.is_valid():
            current_type = add_daily_one_form.cleaned_data['type']
            return redirect('/finance/adddaily/' + str(current_type.pk) + '/')
    else:
        add_daily_one_form = AddDailyOne()
    context = {
        'add_daily_one_form': add_daily_one_form,
    }
    return render(request, 'add_new_daily_one.html', context)


def safes(request, pk):
    current_safe = get_object_or_404(Balance, pk=pk)
    current_farm = Farm.objects.get(farm_name=current_safe.farm.farm_name)
    balance = current_safe.balance
    farm_daily = Daily.objects.filter(farm=current_farm, is_invoice=False)
    all_invoice = Daily.objects.filter(farm=current_farm, is_invoice=True)
    all_buys = []
    all_sells = []
    for item in all_invoice:
        if item.maden != 0:
            all_buys.append(item.maden)
        if item.da2en != 0:
            all_sells.append(item.da2en)
    final_buys = sum(all_buys)
    final_sells = sum(all_sells)
    all_costs = []
    for item in farm_daily:
        if item.maden != 0:
            all_costs.append(item.maden)
    final_costs = sum(all_costs)
    costs = final_costs + final_buys
    net = final_sells - costs

    context = {
        'current_safe': current_safe,
        'balance': balance,
        'farm_daily': farm_daily,
        'final_costs': final_costs,
        'final_buys': final_buys,
        'final_sells': final_sells,
        'net': net,
    }
    return render(request, 'safes.html', context)


def create_invoice_buy(request):
    add_buy_invoice_form = AddBuyInvoice(request.POST)
    if request.method == 'POST':
        if add_buy_invoice_form.is_valid():
            form = add_buy_invoice_form.save(commit=False)
            total = form.quantity * form.price
            form.total_price = total
            form.save()
            new_daily = Daily(text='فاتورة رقم  ' + str(form.id), total_da2en=0, total_maden=form.total_price,
                              type=form.category.type, category=form.category, da2en=0, maden=form.total_price,
                              farm=form.farm, is_invoice=True)
            new_daily.save()
            current_balance = Balance.objects.get(farm=form.farm)
            new_balance = int(current_balance.balance) - int(form.total_price)
            current_balance.balance = new_balance
            current_balance.save()
            current_item = Warehouse.objects.get(item_name=form.product)
            added_quant = int(current_item.item_quantity) + int(form.quantity)
            current_item.item_quantity = added_quant
            current_item.save()
            return redirect('finance_daily')
    else:
        add_buy_invoice_form = AddBuyInvoice()
    context = {
        'add_buy_invoice_form': add_buy_invoice_form,
    }
    return render(request, 'create_buy_invoice.html', context)


def create_invoice_sell(request):
    add_sell_invoice_form = AddSellInvoice(request.POST)
    if request.method == 'POST':
        if add_sell_invoice_form.is_valid():
            form = add_sell_invoice_form.save(commit=False)
            total = form.quantity * form.price
            form.total_price = total
            form.save()
            new_daily = Daily(text='فاتورة رقم  ' + str(form.id), total_da2en=form.total_price, total_maden=0,
                              type=form.category.type, category=form.category, da2en=form.total_price, maden=0,
                              farm=form.farm, is_invoice=True)
            new_daily.save()
            current_balance = Balance.objects.get(farm=form.farm)
            new_balance = int(current_balance.balance) + int(form.total_price)
            current_balance.balance = new_balance
            current_balance.save()
            current_item = Warehouse.objects.get(item_name=form.product)
            added_quant = int(current_item.item_quantity) - int(form.quantity)
            current_item.item_quantity = added_quant
            current_item.save()
            return redirect('finance_daily')
    else:
        add_sell_invoice_form = AddSellInvoice()
    context = {
        'add_sell_invoice_form': add_sell_invoice_form,
    }
    return render(request, 'create_sell_invoice.html', context)


def income_list(request):
    all_invoice = Daily.objects.filter(is_invoice=True)
    all_daily = Daily.objects.filter(is_invoice=False)
    all_sells = []
    all_buys = []
    for item in all_invoice:
        if item.da2en != 0:
            all_sells.append(item.da2en)
        if item.maden != 0:
            all_buys.append(item.maden)
    final_sells = sum(all_sells)
    final_buys = sum(all_buys)
    st_profit = final_sells - final_buys
    all_costs = []
    for item in all_daily:
        if item.da2en != 0:
            all_costs.append(item.da2en)
    final_costs = sum(all_costs)
    net = st_profit - final_costs
    context = {
        'final_sells': final_sells,
        'final_buys': final_buys,
        'st_profit': st_profit,
        'final_costs': final_costs,
        'net': net,
    }

    return render(request, 'income_list.html', context)


def report_all(request):
    all_balance = Balance.objects.all()
    total_bal = []
    for bal in all_balance:
        total_bal.append(bal.balance)
    final_total_bal = sum(total_bal)
    all_sales = SellInvoice.objects.all()
    total_sales = []
    for item in all_sales:
        total_sales.append(item.total_price)
    final_total_sells = sum(total_sales)
    all_buys = BuyInvoice.objects.all()
    total_buy = []
    for item in all_buys:
        total_buy.append(item.total_price)
    final_total_buys = sum(total_buy)
    taxes = 0
    one_net = final_total_sells - taxes
    all_costs = Daily.objects.filter(is_invoice=False)
    costs = []
    for item in all_costs:
        if item.maden != 0:
            costs.append(item.maden)
    final_costs = sum(costs)
    all_costs_and_buys = final_costs + final_total_buys
    final_net = final_total_sells - all_costs_and_buys
    context = {
        'all_balance': all_balance,
        'final_total_bal': final_total_bal,
        'all_sales': all_sales,
        'final_total_sells': final_total_sells,
        'taxes': taxes,
        'one_net': one_net,
        'final_total_buys': final_total_buys,
        'final_costs': final_costs,
        'final_net': final_net,
    }
    return render(request, 'reports/all.html', context)


def report_farm(request):
    farm_report_form = FarmReportForm(request.POST)
    if request.method == 'POST':
        if farm_report_form.is_valid():
            farm_name = farm_report_form.cleaned_data['farm']
            return redirect('/farm/report/details/' + str(farm_name.pk))
    else:
        farm_report_form = FarmReportForm()
    context = {
        'farm_report_form': farm_report_form,
    }
    return render(request, 'reports/farm.html', context)


def report_farm_details(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    current_balance = Balance.objects.get(farm=current_farm).balance
    all_sales = SellInvoice.objects.filter(farm=current_farm)
    total_sales = []
    for item in all_sales:
        total_sales.append(item.total_price)
    final_total_sells = sum(total_sales)
    taxes = 0
    one_net = final_total_sells - taxes
    all_buys = BuyInvoice.objects.filter(farm=current_farm)
    total_buy = []
    for item in all_buys:
        total_buy.append(item.total_price)
    final_total_buys = sum(total_buy)
    all_costs = Daily.objects.filter(is_invoice=False, farm=current_farm)
    costs = []
    for item in all_costs:
        if item.maden != 0:
            costs.append(item.maden)
    final_costs = sum(costs)
    all_costs_and_buys = final_costs + final_total_buys
    final_net = final_total_sells - all_costs_and_buys
    context = {
        'current_farm': current_farm,
        'current_balance': current_balance,
        'final_total_sells': final_total_sells,
        'taxes': taxes,
        'one_net': one_net,
        'final_total_buys': final_total_buys,
        'final_costs': final_costs,
        'final_net': final_net,
    }
    return render(request, 'reports/farm_details.html', context)
