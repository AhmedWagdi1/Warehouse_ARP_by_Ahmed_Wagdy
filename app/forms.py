from django import forms

from app.models import Company, Farm, Job, Worker


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
    class Meta:
        model = Worker
        fields = ['worker_name', 'worker_phone', 'worker_id', 'worker_address', 'worker_job', 'worker_farm']
