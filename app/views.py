# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic.edit import UpdateView
from app.forms import AddCompanyForm, AddFarmForm, AddJobForm, AddWorkerForm, AddSupplierForm, AddClientForm
from app.models import Company, Farm, Job, Worker, Supplier, Client
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


def worker_details(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    context = {
        'current_worker': current_worker,
    }
    return render(request, 'app/worker_details.html', context)


def worker_delete(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    current_worker.delete()
    return redirect('workers')


class WorkerUpdate(UpdateView):
    model = Worker
    fields = ['worker_name', 'worker_phone', 'worker_id', 'worker_address', 'worker_job', 'worker_farm',
              'worker_salary', 'worker_work_date', 'worker_image']
    template_name_suffix = '_update_form'


def worker_archive(request, pk):
    current_worker = get_object_or_404(Worker, pk=pk)
    current_worker.worker_end_time = date.today()
    current_worker.worker_deleted = True
    current_worker.save()
    return redirect('workers')


def old_workers(request):
    old_worker = Worker.objects.filter(worker_deleted=True)
    context = {
        'old_worker': old_worker,
    }
    return render(request, 'app/old_workers.html', context)


def supplier(request):
    all_supply = Supplier.objects.all()
    context = {
        'all_supply': all_supply,
    }
    return render(request, 'app/supplier.html', context)


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


def clients(request):
    all_clients = Client.objects.all()
    context = {
        'all_clients': all_clients,
    }
    return render(request, 'app/clients.html', context)


def clients_add(request):
    add_client_form = AddClientForm(request.POST)
    if request.method == 'POST':
        if add_client_form.is_valid():
            add_client_form.save()
            return redirect('clients')
    else:
        add_client_form = AddClientForm()
    context = {
        'add_client_form':add_client_form,
    }
    return render(request, 'app/clients_add.html', context)


def supplier_delete(request, pk):
    current_supply = get_object_or_404(Supplier, pk=pk)
    current_supply.delete()
    return redirect('supplier')


class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['supplier_name']
    template_name_suffix = '_update_form'


def supplier_details(request, pk):
    current_supply = get_object_or_404(Supplier, pk=pk)
    context = {
        'current_supply':current_supply,
    }
    return render(request, 'app/supplier_details.html', context)


def client_details(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    context = {
        'current_client':current_client,
    }
    return render(request, 'app/client_details.html', context)


def client_delete(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    current_client.delete()
    return redirect('clients')


class ClientUpdate(UpdateView):
    model = Client
    fields = ['client_name']
    template_name_suffix = '_update_form'