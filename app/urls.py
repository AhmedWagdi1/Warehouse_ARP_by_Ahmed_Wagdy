from django.conf.urls import url
from django.urls import path

from app import views
from django.conf import settings
from django.contrib.auth import logout
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.index, name="index"),
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
                  # clients
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
                  url(r'finance/daily/', views.finance_daily, name="finance_daily"),
                  url(r'finance/ostaz/', views.ostaz, name="ostaz"),
                  url(r'finance/adddaily/one', views.add_daily_one, name="add_daily_one"),
                  url(r'finance/adddaily/(?P<pk>[0-9]+)/$', views.add_new_daily, name="add_new_daily"),
                  url(r'ostaz/(?P<pk>[0-9]+)/$', views.ostaz_details, name="ostaz_details"),
                  url(r'mezan/', views.mezan, name="mezan"),
                  url(r'add/tawseef/', views.add_tawseef, name="add_tawseef"),
                  url(r'delete/tawseef/(?P<pk>[0-9]+)/$', views.delete_tawseef, name="delete_tawseef"),
                  url(r'^tawseef/update/(?P<pk>[0-9]+)/', views.TawseefUpdate.as_view(), name="tawseef_update"),
                  url(r'^new/dailu/$', views.new_daily, name="new_daily"),
                  path('finance/mezania/', views.mezania, name="mezania"),
                  path('safe/depost/<int:pk>/', views.safe_deposit, name="safe_deposit"),
                  # ajax_refreshes
                  path('ajax/load-cities/', views.load_cates, name='ajax_load_cates'),  # <-- this one here
                  path('ajax/load-cities_da2en/', views.load_cates_da2en, name='ajax_load_cates_da2en'),
                  # <-- this one here

                  # safes
                  url(r'^safe/(?P<pk>[0-9]+)/', views.safes, name="safes"),
                  # invoice
                  url(r'^create/invoice/buy$', views.create_invoice_buy, name="create_buy_invoice"),
                  url(r'^create/invoice/sell$', views.create_invoice_sell, name="create_sell_invoice"),
                  # income_list
                  url(r'^income/list/', views.income_list, name="income_list"),
                  url(r'^income/list/', views.income_list, name="income_list"),
                  url(r'^report/all/', views.report_all, name="report_all"),
                  url(r'^report/farm/', views.report_farm, name="report_farm"),
                  url(r'^farm/report/details/(?P<pk>[0-9]+)/', views.report_farm_details, name="report_farm_details"),
                  url(r'^report/sales/', views.report_sales, name="report_sales"),
                  url(r'^report/buys/', views.report_buys, name="report_buys"),
                  url(r'^report/daily/', views.report_daily, name="report_daily"),
                  # Warehouses
                  path('warehouse/<int:pk>/', views.warehouse_details, name="warehouse_details"),
                  path('talab/sarf/<int:pk>/', views.talab_sarf, name="talab_sarf"),
                  path('talabat/sarf/list/', views.talab_sarf_list, name="talab_sarf_list"),
                  path('talabat/delete/<int:pk>', views.talabat_delete, name="talabat_delete"),
                  path('talabat/do/<int:pk>/', views.talabat_do, name="talabat_do"),
                  # Users
                  path('users/create/', views.user_create, name="user_create"),
                  path('users/<int:pk>/delete/', views.user_delete, name="user_delete"),
                  # Activation
                  path('activation/request', views.activation_request, name="activation_request"),
                  path('serial/request/done/', views.serial_request_done, name="serial_request_done"),
                  path('activation/', views.activation, name="activation"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
