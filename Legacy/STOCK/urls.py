from django.conf.urls import  include, url
from . import views

app_name = "STOCK"
urlpatterns = [
    # Examples:
    # url(r'^Stock/$', 'ERP.views.home', name='home'),
    # url(r'^Stock/blog/', include('blog.urls')),
    
    url(r'^Stock/$', views.stock_home , name="stock"),
    url(r'^Stock/Add/$', views.stock_add , name="stock_add"),
    url(r'^Stock/Search/$', views.stock_search , name="stock_search"),
    url(r'^Stock/Transfer/$', views.stock_transfer , name="stock_transfer"),
    url(r'^Stock/Warehouses/$', views.stock_warehouse , name="stock_warehouse"),
    url(r'^Stock/Recieve/(?P<trans_id>[0-9]+)/', views.stock_recieve_transfer, name="stock_recieve_transfer"),
    url(r'^Stock/Inventory/$',views.inventory_home, name = "inventory"),
    url(r'^Stock/Inventory/(?P<warehouse_id>[0-9]+)/Print/$',views.inventory_print, name = "print_inventory"),

]


