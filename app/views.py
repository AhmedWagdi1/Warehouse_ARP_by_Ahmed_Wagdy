# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic.edit import UpdateView
from app.forms import AddCompanyForm, AddFarmForm, AddJobForm, AddWorkerForm, AddSupplierForm, AddClientForm, \
    AddProductForm, WarehouseEntryForm, MainFinanceDepositForm, MainFinanceWithdrawForm, SellInvoiceForm, \
    FundsTransfaerForm, BuyInvoiceForm, FarmFinancemoveForm, WorkingCostsForm, ManagementCostsForm, MainMangCosts, \
    MainWorkCosts, AddDailyForm, PickOstazForm
from app.models import Company, Farm, Job, Worker, Supplier, Client, Warehouse, Product, MainFinanceMovement, \
    MainFinance, Balance, FarmFinancemove, SellInvoice, BuyInvoice, WorkingCosts, ManagmentCosts, Daily, Type
from datetime import date, datetime


@login_required
def index(request):
    companys = Company.objects.all()
    all_workers = Worker.objects.filter(worker_deleted=False)
    if not companys:
        return redirect('nocomp')
    else:
        return render(request, 'app/index.html', {'all_workers': all_workers})


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
    company_title = Company.objects.all()[0]
    if request.method == 'POST':
        if add_farm_form.is_valid():
            ad_farm = add_farm_form.save(commit=False)
            ad_farm.farm_company = company_title
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
            return redirect('index')
    else:
        add_worker_form = AddWorkerForm()
    context = {
        'add_worker_form': add_worker_form,
    }

    return render(request, 'app/workers_add.html', context)


@login_required
def jobs_add(request):
    add_job_form = AddJobForm(request.POST)
    company_title = Company.objects.all()[0]
    all_jobs = Job.objects.all()
    if request.method == 'POST':
        if add_job_form.is_valid():
            ad_job = add_job_form.save(commit=False)
            ad_job.job_company = company_title
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
def invoices_sell(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    company = Company.objects.all()[0]
    company_farm = Farm.objects.get(farm_name=company.company_name)
    balance = MainFinance.objects.all()[0]
    sell_invoice_form = SellInvoiceForm(request.POST)
    if request.method == 'POST':
        if sell_invoice_form.is_valid():
            form = sell_invoice_form.save(commit=False)
            form.user = request.user
            form.source = current_farm.farm_name
            form.save()
            current_item = form.product.id
            in_sotorage = Warehouse.objects.get(id=current_item)
            new_amount = in_sotorage.item_quantity - form.quantity
            in_sotorage.item_quantity = new_amount
            in_sotorage.save()
            if form.product2:
                current_item2 = form.product2.id
                in_sotorage2 = Warehouse.objects.get(id=current_item2)
                new_amount2 = in_sotorage2.item_quantity - form.quantity2
                in_sotorage2.item_quantity = new_amount2
                in_sotorage2.save()
            else:
                pass
            if form.product3:
                current_item3 = form.product3.id
                in_sotorage3 = Warehouse.objects.get(id=current_item3)
                new_amount3 = in_sotorage3.item_quantity - form.quantity3
                in_sotorage3.item_quantity = new_amount3
                in_sotorage3.save()
            else:
                pass
            if form.product4:
                current_item4 = form.product4.id
                in_sotorage4 = Warehouse.objects.get(id=current_item4)
                new_amount4 = in_sotorage4.item_quantity - form.quantity4
                in_sotorage4.item_quantity = new_amount4
                in_sotorage4.save()
            else:
                pass
            if form.product5:
                current_item5 = form.product5.id
                in_sotorage5 = Warehouse.objects.get(id=current_item5)
                new_amount5 = in_sotorage5.item_quantity - form.quantity5
                in_sotorage5.item_quantity = new_amount5
                in_sotorage5.save()
            else:
                pass
            if form.product6:
                current_item6 = form.product6.id
                in_sotorage6 = Warehouse.objects.get(id=current_item6)
                new_amount6 = in_sotorage6.item_quantity - form.quantity6
                in_sotorage6.item_quantity = new_amount6
                in_sotorage6.save()
            else:
                pass
            if form.product7:
                current_item7 = form.product7.id
                in_sotorage7 = Warehouse.objects.get(id=current_item7)
                new_amount7 = in_sotorage7.item_quantity - form.quantity7
                in_sotorage7.item_quantity = new_amount7
                in_sotorage7.save()
            else:
                pass
            if form.product8:
                current_item8 = form.product8.id
                in_sotorage8 = Warehouse.objects.get(id=current_item8)
                new_amount8 = in_sotorage8.item_quantity - form.quantity8
                in_sotorage8.item_quantity = new_amount8
                in_sotorage8.save()
            else:
                pass
            if form.product9:
                current_item9 = form.product9.id
                in_sotorage9 = Warehouse.objects.get(id=current_item9)
                new_amount9 = in_sotorage9.item_quantity - form.quantity9
                in_sotorage9.item_quantity = new_amount9
                in_sotorage9.save()
            else:
                pass
            if form.product10:
                current_item10 = form.product10.id
                in_sotorage10 = Warehouse.objects.get(id=current_item10)
                new_amount10 = in_sotorage10.item_quantity - form.quantity10
                in_sotorage10.item_quantity = new_amount10
                in_sotorage10.save()
            else:
                pass
            if current_farm == company_farm:
                new_entry_main = MainFinanceMovement(mode=2, user=request.user, text=form.id, amount=form.total)
                new_entry_main.save()
                current_balance = balance.balance
                added_balance = form.total
                new_balance = current_balance + added_balance
                balance.balance = new_balance
                balance.save()
                return redirect('finance_main')
            else:
                current_balance = Balance.objects.get(farm=current_farm)
                added_balance = current_balance.balance + form.total
                current_balance.balance = added_balance
                current_balance.save()
                new_entry = FarmFinancemove(mode=2, user=request.user, text=form.id, amount=form.total,
                                            farm=current_farm)
                new_entry.save()
                return HttpResponseRedirect('/finance/farms/' + str(current_farm.pk) + '/')
    else:
        sell_invoice_form = SellInvoiceForm()

    context = {
        'company': company,
        'current_farm': current_farm,
        'sell_invoice_form': sell_invoice_form,
    }
    return render(request, 'app/invoice_sell.html', context)


@login_required
def invoices_buy(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    company = Company.objects.all()[0]
    company_farm = Farm.objects.get(farm_name=company.company_name)
    balance = MainFinance.objects.all()[0]
    buy_invoice_form = BuyInvoiceForm(request.POST)
    if request.method == 'POST':
        if buy_invoice_form.is_valid():
            form = buy_invoice_form.save(commit=False)
            form.user = request.user
            if current_farm == company_farm:
                form.source = current_farm.farm_company.company_name
            else:
                form.source = current_farm.farm_name
            form.save()
            current_item = form.product.id
            in_sotorage = Product.objects.get(id=current_item)
            if Warehouse.objects.filter(id=current_item).count() != 0:
                newit = Warehouse.objects.get(id=current_item)
                new_amount = newit.item_quantity + form.quantity
                newit.item_quantity = new_amount
                newit.save()
            else:
                newz = Warehouse(item_name=in_sotorage, item_quantity=form.quantity)
                newz.save()
            if form.product2:
                current_item2 = form.product2.id
                in_sotorage2 = Product.objects.get(id=current_item2)
                if Warehouse.objects.filter(id=current_item2) != 0:
                    newit = Warehouse.objects.get(id=current_item2)
                    new_amount2 = newit.item_quantity + form.quantity2
                    newit.item_quantity = new_amount2
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage2, item_quantity=form.quantity2)
                    news.save()
            else:
                pass
            if form.product3:
                current_item3 = form.product3.id
                in_sotorage3 = Product.objects.get(id=current_item3)
                if Warehouse.objects.filter(id=current_item3) != 0:
                    newit = Warehouse.objects.get(id=current_item3)
                    new_amount3 = newit.item_quantity + form.quantity3
                    newit.item_quantity = new_amount3
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage3, item_quantity=form.quantity3)
                    news.save()
            else:
                pass
            if form.product4:
                current_item4 = form.product4.id
                in_sotorage4 = Product.objects.get(id=current_item4)
                if Warehouse.objects.filter(id=current_item4) != 0:
                    newit = Warehouse.objects.get(id=current_item4)
                    new_amount4 = newit.item_quantity + form.quantity4
                    newit.item_quantity = new_amount4
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage4, item_quantity=form.quantity4)
                    news.save()
            else:
                pass
            if form.product5:
                current_item5 = form.product5.id
                in_sotorage5 = Product.objects.get(id=current_item5)
                if Warehouse.objects.filter(id=current_item5) != 0:
                    newit = Warehouse.objects.get(id=current_item5)
                    new_amount5 = newit.item_quantity + form.quantity5
                    newit.item_quantity = new_amount5
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage5, item_quantity=form.quantity5)
                    news.save()
            else:
                pass
            if form.product6:
                current_item6 = form.product6.id
                in_sotorage6 = Product.objects.get(id=current_item6)
                if Warehouse.objects.filter(id=current_item6) != 0:
                    newit = Warehouse.objects.get(id=current_item6)
                    new_amount6 = newit.item_quantity + form.quantity6
                    newit.item_quantity = new_amount6
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage6, item_quantity=form.quantity6)
                    news.save()
            else:
                pass
            if form.product7:
                current_item7 = form.product7.id
                in_sotorage7 = Product.objects.get(id=current_item7)
                if Warehouse.objects.filter(id=current_item7) != 0:
                    newit = Warehouse.objects.get(id=current_item7)
                    new_amount7 = newit.item_quantity + form.quantity7
                    newit.item_quantity = new_amount7
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage7, item_quantity=form.quantity7)
                    news.save()
            else:
                pass
            if form.product8:
                current_item8 = form.product8.id
                in_sotorage8 = Product.objects.get(id=current_item8)
                if Warehouse.objects.filter(id=current_item8) != 0:
                    newit = Warehouse.objects.get(id=current_item8)
                    new_amount8 = newit.item_quantity + form.quantity8
                    newit.item_quantity = new_amount8
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage8, item_quantity=form.quantity8)
                    news.save()
            else:
                pass
            if form.product9:
                current_item9 = form.product9.id
                in_sotorage9 = Product.objects.get(id=current_item9)
                if Warehouse.objects.filter(id=current_item9) != 0:
                    newit = Warehouse.objects.get(id=current_item9)
                    new_amount9 = newit.item_quantity + form.quantity9
                    newit.item_quantity = new_amount9
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage9, item_quantity=form.quantity9)
                    news.save()
            else:
                pass
            if form.product10:
                current_item10 = form.product10.id
                in_sotorage10 = Product.objects.get(id=current_item10)
                if Warehouse.objects.filter(id=current_item10) != 0:
                    newit = Warehouse.objects.get(id=current_item10)
                    new_amount10 = newit.item_quantity + form.quantity10
                    newit.item_quantity = new_amount10
                    newit.save()
                else:
                    news = Warehouse(item_name=in_sotorage10, item_quantity=form.quantity10)
                    news.save()
            else:
                pass

            if current_farm == company_farm:
                current_balance = balance.balance
                added_balance = form.total
                new_balance = current_balance - added_balance
                balance.balance = new_balance
                balance.save()
                return redirect('finance_main')
            else:
                current_balance = Balance.objects.get(farm=current_farm)
                added_balance = current_balance.balance - form.total
                current_balance.balance = added_balance
                current_balance.save()
                new_entry = FarmFinancemove(mode=1, user=request.user, text=form.id, amount=form.total,
                                            farm=current_farm)
                new_entry.save()
                return HttpResponseRedirect('/finance/farms/' + str(current_farm.pk) + '/')
    else:
        buy_invoice_form = BuyInvoiceForm()
    context = {
        'company': company,
        'current_farm': current_farm,
        'buy_invoice_form': buy_invoice_form,
    }
    return render(request, 'app/invoice_buy.html', context)


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


@login_required
def finance_main(request):
    all_movments = MainFinanceMovement.objects.all()
    current_balance = MainFinance.objects.all()[0]
    company_name = Company.objects.all()[0]
    current_farm = Farm.objects.get(farm_name=company_name.company_name)
    this_farm_buys = BuyInvoice.objects.filter(source=company_name.company_name)
    all_buy = []
    for item in this_farm_buys:
        all_buy.append(item.total)
    final_all_buy = sum(all_buy)

    this_farm_sells = SellInvoice.objects.filter(source=company_name.company_name)
    all_sell = []
    for item in this_farm_sells:
        all_sell.append(item.total)
    final_all_sell = sum(all_sell)

    this_farm_cost = MainFinanceMovement.objects.filter(mode=1).exclude(text='تحويل لمزرعة ')
    all_cost = []
    for item in this_farm_cost:
        all_cost.append(item.amount)
    final_all_cost = sum(all_cost)

    net = final_all_sell - (final_all_cost + final_all_buy)

    context = {
        'all_movments': all_movments,
        'current_balance': current_balance,
        'current_farm': current_farm,
        'final_all_buy': final_all_buy,
        'final_all_sell': final_all_sell,
        'final_all_cost': final_all_cost,
        'net': net,
    }
    return render(request, 'app/finance_main.html', context)


@login_required
def finance_main_deposit(request):
    current_balance = MainFinance.objects.all()[0]
    main_finance_deposit_form = MainFinanceDepositForm(request.POST)
    if request.method == 'POST':
        if main_finance_deposit_form.is_valid():
            form = main_finance_deposit_form.save(commit=False)
            form.mode = 2
            form.user = request.user
            form.save()
            old = current_balance.balance
            new = form.amount
            total = old + new
            current_balance.balance = total
            current_balance.save()
            return redirect('finance_main')
    else:
        main_finance_deposit_form = MainFinanceDepositForm()
    context = {
        'main_finance_deposit_form': main_finance_deposit_form,
    }
    return render(request, 'app/finance_main_deposit.html', context)


@login_required
def finance_main_withdraw(request):
    current_balance = MainFinance.objects.all()[0]
    main_finance_withdraw_form = MainFinanceWithdrawForm(request.POST)
    if request.method == 'POST':
        if main_finance_withdraw_form.is_valid():
            form = main_finance_withdraw_form.save(commit=False)
            form.mode = 1
            form.user = request.user
            form.save()
            old = current_balance.balance
            new = form.amount
            total = old - new
            current_balance.balance = total
            current_balance.save()
            return redirect('finance_main')
    else:
        main_finance_withdraw_form = MainFinanceWithdrawForm()
    context = {
        'main_finance_withdraw_form': main_finance_withdraw_form,
    }
    return render(request, 'app/finance_main_withdraw.html', context)


@login_required
def farms_finance(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    bal = Balance.objects.get(farm=current_farm)
    all_movement = FarmFinancemove.objects.filter(farm=current_farm)
    this_farm_sell = SellInvoice.objects.filter(source=current_farm.farm_name)
    all_sells = []
    for item in this_farm_sell:
        all_sells.append(item.total)
    final_all_sells = sum(all_sells)

    this_farm_buy = BuyInvoice.objects.filter(source=current_farm.farm_name)
    all_buy = []
    for item in this_farm_buy:
        all_buy.append(item.total)
    final_all_buy = sum(all_buy)

    this_farm_costs = FarmFinancemove.objects.filter(farm=current_farm, mode=1, cost=True)
    all_cost = []
    for item in this_farm_costs:
        all_cost.append(item.amount)
    final_all_cost = sum(all_cost)

    net = final_all_sells - (final_all_buy + final_all_cost)
    context = {
        'current_farm': current_farm,
        'bal': bal,
        'all_movement': all_movement,
        'final_all_sells': final_all_sells,
        'final_all_buy': final_all_buy,
        'final_all_cost': final_all_cost,
        'net': net,
    }
    return render(request, 'app/farms_finance.html', context)


@login_required
def trasnfaer_farm(request):
    farm_transfer_form = FundsTransfaerForm(request.POST)
    selected_amount = request.POST.get('amount')
    if request.method == 'POST':
        if farm_transfer_form.is_valid():
            selected_farm = farm_transfer_form.cleaned_data['farms']
            the_farm = Balance.objects.get(farm=selected_farm)
            current_farm_balance = the_farm.balance
            new_farm_balance = int(current_farm_balance) + int(selected_amount)
            the_farm.balance = new_farm_balance
            the_farm.save()
            main = MainFinance.objects.all()[0]
            current_main_balance = main.balance
            new_main_balance = int(current_main_balance) - int(selected_amount)
            main.balance = new_main_balance
            new_main_move = MainFinanceMovement(mode=1, user=request.user, text='تحويل لمزرعة ',
                                                amount=selected_amount)
            new_main_move.save()
            main.save()
            new_farm_move = FarmFinancemove(mode=2, user=request.user, text='تحويل من الشركة', amount=selected_amount,
                                            farm=selected_farm)
            new_farm_move.save()
            return redirect('finance_main')
    else:
        farm_transfer_form = FundsTransfaerForm()
    context = {
        'farm_transfer_form': farm_transfer_form,
    }
    return render(request, 'app/transfer_farm.html', context)


@login_required
def farm_costs(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    farm_finance_move_form = FarmFinancemoveForm(request.POST)
    if request.method == 'POST':
        if farm_finance_move_form.is_valid():
            form = farm_finance_move_form.save(commit=False)
            form.mode = 1
            form.user = request.user
            form.farm = current_farm
            form.cost = True
            form.save()
            current_balance = Balance.objects.get(farm=current_farm)
            old_balance = current_balance.balance
            added_balance = form.amount
            new_balance = old_balance - added_balance
            current_balance.balance = new_balance
            current_balance.save()
            return HttpResponseRedirect('/finance/farms/' + str(current_farm.pk) + '/')
    else:
        farm_finance_move_form = FarmFinancemoveForm()

    context = {
        'farm_finance_move_form': farm_finance_move_form,
    }
    return render(request, 'app/farm_withd.html', context)


def mangcosts_farm_withd(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    main_manage_cost_form = MainMangCosts(request.POST)
    if request.method == 'POST':
        if main_manage_cost_form.is_valid():
            current_balance = Balance.objects.get(farm=current_farm)
            old_balance = current_balance.balance
            added_balance = main_manage_cost_form.cleaned_data['amount']
            new_balance = old_balance - added_balance
            current_balance.balance = new_balance
            current_balance.save()
            new_move = FarmFinancemove(mode=1, user=request.user, text=main_manage_cost_form.cleaned_data['type'],
                                       amount=added_balance, farm=current_farm, cost=True)
            new_move.save()
            return HttpResponseRedirect('/finance/farms/' + str(current_farm.pk) + '/')
    else:
        main_manage_cost_form = MainMangCosts()

    context = {
        'main_manage_cost_form': main_manage_cost_form,
    }
    return render(request, 'app/farm_mang_costs.html', context)


def workcosts_farm_withd(request, pk):
    current_farm = get_object_or_404(Farm, pk=pk)
    farm_work_cost_form = MainWorkCosts(request.POST)
    if request.method == 'POST':
        if farm_work_cost_form.is_valid():
            current_balance = Balance.objects.get(farm=current_farm)
            old_balance = current_balance.balance
            added_balance = farm_work_cost_form.cleaned_data['amount']
            new_balance = old_balance - added_balance
            current_balance.balance = new_balance
            current_balance.save()
            new_move = FarmFinancemove(mode=1, user=request.user, text=farm_work_cost_form.cleaned_data['type'],
                                       amount=added_balance, farm=current_farm, cost=True)
            new_move.save()
            return HttpResponseRedirect('/finance/farms/' + str(current_farm.pk) + '/')
    else:
        farm_work_cost_form = MainWorkCosts()

    context = {
        'farm_work_cost_form': farm_work_cost_form,
    }
    return render(request, 'app/farm_work_costs.html', context)


@login_required
def main_center(request):
    main_movment = MainFinanceMovement.objects.all()
    farm_movment = FarmFinancemove.objects.all()
    # getting all buy
    all_buy = BuyInvoice.objects.all()
    all_buy_list = []
    for item in all_buy:
        all_buy_list.append(item.total)
    final_all_buy = sum(all_buy_list)
    # getting all_sell
    all_sell = SellInvoice.objects.all()
    all_sell_list = []
    for item in all_sell:
        all_sell_list.append(item.total)
    final_all_sell = sum(all_sell_list)
    # getting_all_costs
    main_costs = MainFinanceMovement.objects.filter(mode=1)
    main_costs_list = []
    for item in main_costs:
        main_costs_list.append(item.amount)
    final_main_costs = sum(main_costs_list)
    ########################################
    farm_cost = FarmFinancemove.objects.filter(mode=1)
    farm_cost_list = []
    for item in farm_cost:
        farm_cost_list.append(item.amount)
    final_farm_costs = sum(farm_cost_list)
    total_costs = final_main_costs + final_farm_costs
    from itertools import chain
    #####################################
    net = final_all_sell - (final_all_buy + total_costs)
    result_list = sorted(chain(main_movment, farm_movment),
                         key=lambda instance: instance.date)
    context = {
        'result_list': result_list,
        'final_all_buy': final_all_buy,
        'final_all_sell': final_all_sell,
        'total_costs': total_costs,
        'net': net,
    }
    return render(request, 'app/main_center.html', context)


@login_required
def add_work_cost(request):
    all_working_costs = WorkingCosts.objects.all()
    add_working_cost_form = WorkingCostsForm(request.POST)
    if request.method == 'POST':
        if add_working_cost_form.is_valid():
            add_working_cost_form.save()
            return redirect('add_work_cost')
    else:
        add_working_cost_form = WorkingCostsForm()
    context = {
        'add_working_cost_form': add_working_cost_form,
        'all_working_costs': all_working_costs,
    }
    return render(request, 'app/add_work_costs.html', context)


@login_required
def delete_work_cost(request, pk):
    current_work_costs = get_object_or_404(WorkingCosts, pk=pk)
    current_work_costs.delete()
    return redirect('add_work_cost')


class WorkingCostsUpdate(UpdateView):
    model = WorkingCosts
    fields = ['name']
    template_name_suffix = '_update_form'


@login_required
def add_mang_cost(request):
    mang_cost_add_form = ManagementCostsForm(request.POST)
    all_mang_costs = ManagmentCosts.objects.all()
    if request.method == 'POST':
        if mang_cost_add_form.is_valid():
            mang_cost_add_form.save()
            return redirect('add_mang_cost')
    else:
        mang_cost_add_form = ManagementCostsForm()
    context = {
        'mang_cost_add_form': mang_cost_add_form,
        'all_mang_costs': all_mang_costs,
    }
    return render(request, 'app/add_mang_costs.html', context)


@login_required
def delete_mang_cost(request, pk):
    current_mang_cost = get_object_or_404(ManagmentCosts, pk=pk)
    current_mang_cost.delete()
    return redirect('add_mang_cost')


class MangCostsUpdate(UpdateView):
    model = ManagmentCosts
    fields = ['name']
    template_name_suffix = '_update_form'


def mangcosts_main_withd(request):
    current_balance = MainFinance.objects.all()[0]
    main_mang_costs_with_form = MainMangCosts(request.POST)
    if request.method == 'POST':
        if main_mang_costs_with_form.is_valid():
            old_balance = current_balance.balance
            added_balance = main_mang_costs_with_form.cleaned_data['amount']
            new_balance = old_balance - added_balance
            current_balance.balance = new_balance
            current_balance.save()
            new_move = MainFinanceMovement(mode=1, user=request.user,
                                           text=main_mang_costs_with_form.cleaned_data['type'], amount=added_balance)
            new_move.save()
            return redirect('finance_main')
    else:
        main_mang_costs_with_form = MainMangCosts()
    context = {
        'main_mang_costs_with_form': main_mang_costs_with_form,
    }
    return render(request, 'app/mang_costs_main_withd.html', context)


def workcosts_main_withd(request):
    current_balance = MainFinance.objects.all()[0]
    main_work_costs_with_form = MainWorkCosts(request.POST)
    if request.method == 'POST':
        if main_work_costs_with_form.is_valid():
            old_balance = current_balance.balance
            added_balance = main_work_costs_with_form.cleaned_data['amount']
            new_balance = old_balance - added_balance
            current_balance.balance = new_balance
            current_balance.save()
            new_move = MainFinanceMovement(mode=1, user=request.user,
                                           text=main_work_costs_with_form.cleaned_data['type'], amount=added_balance)
            new_move.save()
            return redirect('finance_main')
    else:
        main_work_costs_with_form = MainWorkCosts()
    context = {
        'main_work_costs_with_form': main_work_costs_with_form,
    }
    return render(request, 'app/work_costs_main_withd.html', context)


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
            current_type = pick_ostaz_form.cleaned_data['type']
            return redirect('ostaz_details', pk=current_type.pk)
    else:
        pick_ostaz_form = PickOstazForm()
    context = {
        'pick_ostaz_form': pick_ostaz_form,
    }
    return render(request, 'ostaz.html', context)


def ostaz_details(request, pk):
    current_type = get_object_or_404(Type, pk=pk)
    context = {
        'current_type': current_type,
    }
    return render(request, 'ostaz_details.html', context)
