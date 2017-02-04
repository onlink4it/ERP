from django.conf.urls import url,static
from . import views

app_name = 'DELIVERY'

urlpatterns = [
    url(r'^$',views.Delivery_home,name="delivery"),
    url(r'^Invoice/Customer/(?P<customer_id>[0-9]+)/New_Address/$',views.Delivery_add_address, name="delivery_add_address"),
    url(r'^Invoice/Customer/(?P<customer_id>[0-9]+)/$',views.Delivery_add_invoice, name="delivery_add_invoice"),
    url(r'^Invoice/Customer/(?P<customer_id>[0-9]+)/Edit/$',views.Delivery_customer_edit,name="delivery_customer_edit"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Categories/$',views.Delivery_categories,name="delivery_categories"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Categories/(?P<cat_id>[0-9]+)/$',views.Delivery_items,name="delivery_items"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Item/(?P<item_id>[0-9]+)/$',views.Delivery_add_item,name="delivery_add_item"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Increase/(?P<inv_item_id>[0-9]+)/$',views.Delivery_increase_quantity,name="delivery_increase_quantity"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Decrease/(?P<inv_item_id>[0-9]+)/$',views.Delivery_decrease_quantity,name="delivery_decrease_quantity"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Delete/(?P<inv_item_id>[0-9]+)/$',views.Delivery_delete_invoice_item,name="delivery_delete_invoice_item"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Delete/Invoice/$',views.Delivery_delete_invoice,name="delivery_delete_invoice"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Close/$',views.Delivery_close_invoice, name="delivery_close_invoice"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Print/$',views.Delivery_print_invoice, name="delivery_print_invoice"),   
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Ship/$',views.Delivery_shipping, name="delivery_shipping"),   
   ]