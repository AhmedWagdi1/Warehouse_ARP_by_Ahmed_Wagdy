from django.conf.urls import url
from app import views
from django.conf import settings
from django.contrib.auth import logout
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.main_center, name='index'),
                  url(r'^workers/$', views.workers, name="workers"),
                  url(r'^nocomp/$', views.nocomp, name="nocomp"),
                  # company
                  url(r'^add/company/', views.add_company, name="add_company"),
                  # farm
                  url(r'^add/farm/', views.add_farm, name="add_farm"),
                  url(r'^farm/(?P<pk>[0-9]+)/$', views.farm_details, name="farm_details"),
                  url(r'^farm/(?P<pk>[0-9]+)/delete/$', views.farm_delete, name="farm_delete"),
                  url(r'^farm/(?P<pk>[0-9]+)/update/$', views.FarmUpdate.as_view(), name="farm_update"),
                  # jobs
                  url(r'^jobs/add$', views.jobs_add, name="jobs_add"),
                  url(r'^job/(?P<pk>[0-9]+)/delete/$', views.job_delete, name="job_delete"),
                  url(r'^job/(?P<pk>[0-9]+)/update/$', views.JobUpdate.as_view(success_url="/jobs/add"),
                      name="job_update"),
                  # workers
                  url(r'^workers/add$', views.workers_add, name="workers_add"),
                  url(r'^worker/(?P<pk>[0-9]+)/details/$', views.worker_details, name="worker_details"),
                  url(r'^worker/(?P<pk>[0-9]+)/delete/$', views.worker_delete, name="worker_delete"),
                  url(r'^worker/(?P<pk>[0-9]+)/update/$', views.WorkerUpdate.as_view(), name="worker_update"),
                  url(r'^worker/(?P<pk>[0-9]+)/archive/$', views.worker_archive, name="worker_archive"),
                  url(r'^worker/old/$', views.old_workers, name="old_workers"),
                  # supplier
                  url(r'^supplier/$', views.supplier, name="supplier"),
                  url(r'^supplier/add/$', views.supplier_add, name="supplier_add"),
                  url(r'^supplier/delete/(?P<pk>[0-9]+)/', views.supplier_delete, name="supplier_delete"),
                  url(r'^supplier/update/(?P<pk>[0-9]+)/', views.SupplierUpdate.as_view(), name="supplier_update"),
                  url(r'^supplier/details/(?P<pk>[0-9]+)/$', views.supplier_details, name="supplier_details"),

                  #                 clients
                  url(r'^clients/$', views.clients, name="clients"),
                  url(r'^clients/add/$', views.clients_add, name="clients_add"),
                  url(r'^clients/details/(?P<pk>[0-9]+)/$', views.client_details, name="client_details"),
                  url(r'^client/delete/(?P<pk>[0-9]+)/', views.client_delete, name="client_delete"),
                  url(r'^client/update/(?P<pk>[0-9]+)/', views.ClientUpdate.as_view(), name="client_update"),
                  # storages
                  url(r'^warehouse/$', views.warehouse, name="warehouse"),
                  url(r'^wharehouse/entry/$', views.warehouse_entry, name="warehouse_entry"),
                  url(r'^warehouse/(?P<pk>[0-9]+)/out/$', views.warehouse_out, name="warehouse_out"),
                  # products
                  url(r'^products/$', views.product, name="product"),
                  url(r'^products/add/$', views.product_add, name="product_add"),
                  url(r'^product/(?P<pk>[0-9]+)/details', views.product_details, name="product_details"),
                  url(r'^product/(?P<pk>[0-9]+)/delete', views.product_delete, name="product_delete"),
                  url(r'^product/update/(?P<pk>[0-9]+)/', views.ProductUpdate.as_view(), name="product_update"),
                  # finance
                  url(r'^finance/main/$', views.finance_main, name="finance_main"),
                  url(r'^finance/main/deposite/$', views.finance_main_deposit, name="finance_main_deposit"),
                  url(r'^finance/main/withdraw/$', views.finance_main_withdraw, name="finance_main_withdraw"),
                  url(r'^finance/farms/(?P<pk>[0-9]+)/', views.farms_finance, name="farms_finance"),
                  url(r'^finance/transfer/$', views.trasnfaer_farm, name="transfaer_farm"),
                  url(r'^finance/farms/costs/(?P<pk>[0-9]+)/$', views.farm_costs, name="farm_costs"),
                  url(r'^finance/workcosts/add/$', views.add_work_cost, name="add_work_cost"),
                  url(r'^finance/workcosts/delete/(?P<pk>[0-9]+)/$', views.delete_work_cost, name="delete_work_cost"),
                  url(r'^finance/workcosts/update/(?P<pk>[0-9]+)/$', views.WorkingCostsUpdate.as_view(), name="update_work_cost"),
                  url(r'^finance/managementcosts/add/$', views.add_mang_cost, name="add_mang_cost"),
                  # invoices
                  url(r'^invoices/sell/(?P<pk>[0-9]+)/$', views.invoices_sell, name="invoices_sell"),
                  url(r'^invoices/buy/(?P<pk>[0-9]+)/$', views.invoices_buy, name="invoices_buy"),
                  # centers
                  url(r'^main/center/', views.main_center, name="main_center"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
