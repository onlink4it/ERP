from django.conf.urls import  include, url
from . import views

app_name = "STOCK"
urlpatterns = [
    # Examples:
    # url(r'^$', 'ERP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.stock_home , name="stock"),
    url(r'^Add/$', views.stock_add , name="stock_add"),
    url(r'^Search/$', views.stock_search , name="stock_search"),
    url(r'^Transfer/$', views.stock_transfer , name="stock_transfer"),
    url(r'^Warehouses/$', views.stock_warehouse , name="stock_warehouse"),
    url(r'^Recieve/(?P<trans_id>[0-9]+)/', views.stock_recieve_transfer, name="stock_recieve_transfer"),
    url(r'^Inventory/$',views.inventory_home, name = "inventory"),
    url(r'^Inventory/(?P<warehouse_id>[0-9]+)/Print/$',views.inventory_print, name = "print_inventory"),

]


