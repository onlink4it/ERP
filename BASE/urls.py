from django.conf.urls import url,static,include
from . import views

app_name = 'BASE'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$',views.login_user, name="login_user"),
    url(r'logout/$',views.logout_user, name="logout_user"),
    url(r'^System_Setting/$', views.system_setting, name = "system_setting"),
    url(r'^System_Setting/Categories/Add/$', views.add_category, name = "add_category"),
    url(r'^System_Setting/Products/Add/$', views.add_product, name = "add_product"),
    ]
