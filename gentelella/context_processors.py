import datetime

from app.models import Company, Farm, Job


def include_company(request):
    company_name = Company.objects.all()
    if len(company_name) == 0:
        context = {'company_name': company_name}
    else:
        company_title = Company.objects.all()[0]
        context = {
            'company_name': company_name,
            'company_title': company_title,
        }
    return (context)


def include_farm(request):
    all_farms = Farm.objects.all()
    context = {
        'all_farms': all_farms,
    }
    return (context)


def include_job(request):
    all_jobs = Job.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return (context)


def include_current_time(request):
    now = datetime.datetime.now()
    context = {
        'now': now,
    }
    return (context)
