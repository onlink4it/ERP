from django.conf.urls import url,static,include
from . import views

app_name = 'BASE'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$',views.login_user, name="login_user"),
    url(r'logout/$',views.logout_user, name="logout_user"),
    url(r'^Accounts/$',views.accounts_home, name= "accounts_home"),
    url(r'^Accounts/Expenses/Categories/$',views.add_expense_category, name="add_expense_category"),
    #url(r'^Accounts/Expenses/Categories/(?P<cat_id>[0-9]+)/Edit/$',views.edit_expense_category, name="edit_expense_category"),
    url(r'^Accounts/Expenses/Categories/(?P<cat_id>[0-9]+)/Delete/$',views.delete_expense_category, name="delete_expense_category"),
    url(r'^Accounts/Expenses/$',views.add_expense, name="add_expense"),
    url(r'^Accounts/Expenses/(?P<expense_id>[0-9]+)/Edit/$',views.edit_expense, name="edit_expense"),
    url(r'^Accounts/Expenses/(?P<expense_id>[0-9]+)/Delete/$',views.delete_expense, name="delete_expense"),
    url(r'^Accounts/Treasury/$',views.treasury, name="treasury"),
    url(r'^System_Setting/$', views.system_setting, name = "system_setting"),
    url(r'^System_Setting/Categories/Add/$', views.add_category, name = "add_category"),
    url(r'^System_Setting/Products/Add/$', views.add_product, name = "add_product"),
    url(r'^System_Setting/Products/(?P<product_id>[0-9]+)/Edit/$', views.edit_product, name = "edit_product"),
    url(r'^System_Setting/Employees/$',views.user_accounts, name="user_accounts"),
    url(r'^System_Setting/Employees/(?P<user_id>[0-9]+)/$',views.user_perm, name="user_perm"),
    url(r'^Branches/$',views.create_branch,name="branches"),
    url(r'^Branches/(?P<link_id>[0-9]+)/Delete/$',views.delete_branch,name="delete_branch"),
    url(r'^Branches/Choose/$',views.choose_branch,name="choose_branch"),
    url(r'^Stock/$', views.stock_home , name="stock"),
    url(r'^Stock/Add/$', views.stock_add , name="stock_add"),
    url(r'^Stock/Search/$', views.stock_search , name="stock_search"),
    url(r'^Stock/Transfer/$', views.stock_transfer , name="stock_transfer"),
    url(r'^Stock/Warehouses/$', views.stock_warehouse , name="stock_warehouse"),
    url(r'^Stock/Recieve/(?P<trans_id>[0-9]+)/', views.stock_recieve_transfer, name="stock_recieve_transfer"),
    url(r'^Stock/Inventory/$',views.inventory_home, name = "inventory"),
    url(r'^Stock/Inventory/(?P<warehouse_id>[0-9]+)/Print/$',views.inventory_print, name = "print_inventory"),

    ]
