from django.conf.urls import url,static
from . import views

app_name = 'PURCHASES'

urlpatterns = [
    url(r'^$',views.purchase_home,name="purchase"),
    url(r'^Suppliers/$',views.purchase_supplier,name="purchase_supplier"),
    url(r'^Suppliers/(?P<supplier_id>[0-9]+)/Payment/$',views.purchase_supplier_payment,name="purchase_supplier_payment"),
    url(r'^Invoice/$',views.purchase_add_invoice, name="purchase_add_invoice"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/$',views.purchase_invoice_item,name="purchase_add_item"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Delivered/$',views.purchase_invoice_delivered,name="purchase_invoice_delivered"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Item/(?P<item_id>[0-9]+)/Delete$',views.purchase_item_delete,name="purchase_item_delete"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Print/$',views.purchase_print_invoice,name="purchase_print_invoice"),
    ]