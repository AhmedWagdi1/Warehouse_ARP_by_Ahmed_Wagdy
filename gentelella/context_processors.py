import datetime
from django.core.management import call_command
from app.models import Company, Farm, Job, Balance, Talabat, Account,Activation


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


def include_farm_no_company(request):
    all_farms_no_company = Farm.objects.all()[1:]
    context = {
        'all_farms_no_company': all_farms_no_company,
    }
    return (context)


def include_balances(request):
    all_balance = Balance.objects.all()
    context = {
        'all_balance': all_balance,
    }
    return (context)

def include_talabat(request):
    all_talabat = Talabat.objects.filter(OK=False)
    context = {
    'all_talabat':all_talabat,
    }
    return (context)


def get_current_role(request):
    current_role = 'h'
    if request.user.is_authenticated:
        current_user = request.user
        current_role1 = Account.objects.get(user=current_user)
        current_role = current_role1.role
    else:
        pass

    context = {
    'current_role':current_role,
    }
    return (context)

'''
def get_activation_status(request):
    today = datetime.datetime.now()
    activated = False
    check = Activation.objects.filter()
    if check.count() != 0:
        if check[0].is_active:
            activated = True
        else:
            activated = False
            if check[0].last_time.day != today.day:
                call_command('clear_models')
                instance = check[0]
                instance.last_time = today
                instance.save()
            else:
                pass
    else:
        pass
    context = {
    'activated':activated,
    }
    return (context)
'''