from django.conf.urls import url,static
from . import views

app_name = 'POS'

urlpatterns = [
    url(r'^$',views.POS_home,name="POS"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Categories/$',views.POS_categories,name="POS_categories"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Categories/(?P<cat_id>[0-9]+)/$',views.POS_items,name="POS_items"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Item/(?P<item_id>[0-9]+)/$',views.POS_add_item,name="POS_add_item"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Increase/(?P<inv_item_id>[0-9]+)/$',views.POS_increase_quantity,name="POS_increase_quantity"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Decrease/(?P<inv_item_id>[0-9]+)/$',views.POS_decrease_quantity,name="POS_decrease_quantity"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Delete/(?P<inv_item_id>[0-9]+)/$',views.POS_delete_invoice_item,name="POS_delete_invoice_item"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Delete/Invoice/$',views.POS_delete_invoice,name="POS_delete_invoice"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Close/$',views.POS_close_invoice, name="POS_close_invoice"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Pay/$',views.POS_pay_invoice, name="POS_pay_invoice"),
    url(r'^Invoice/(?P<inv_id>[0-9]+)/Print/$',views.POS_print_invoice, name="POS_print_invoice"),
    url(r'^Customer/Add/$',views.POS_add_customer , name="POS_add_customer"),
    url(r'^Customer/(?P<customer_id>[0-9]+)/Payment/$',views.POS_customer_payment , name="POS_customer_payment"),
    url(r'^Customer/(?P<customer_id>[0-9]+)/Delete/$',views.POS_delete_customer , name="POS_delete_customer"),
    url(r'^Employee/(?P<emp_id>[0-9]+)/Payment/$',views.POS_employee_payment , name="POS_employee_payment"),
    ]
