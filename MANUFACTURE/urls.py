from django.conf.urls import url,static
from . import views

app_name = 'MANUFACTURE'

urlpatterns = [
    url(r'^$',views.home,name="manufacture"),
    url(r'^Order/$',views.new_order, name="new_order"),
    url(r'^Order/(?P<order_id>[0-9]+)/Raw_Materials/$', views.raw_materials, name="raw_materials"),
    url(r'^Order/(?P<order_id>[0-9]+)/Raw_Materials/(?P<raw_id>[0-9]+)/Delete/$', views.delete_raw_materials, name="delete_raw_materials"),
    url(r'^Order/(?P<order_id>[0-9]+)/End_Products/$', views.end_products, name="end_products"),
    url(r'^Order/(?P<order_id>[0-9]+)/End_Products/(?P<end_id>[0-9]+)/Delete/$', views.delete_end_products, name="delete_end_products"),
    url(r'^Order/(?P<order_id>[0-9]+)/Start/$', views.start_production, name="start_production"),
    url(r'^Order/(?P<order_id>[0-9]+)/Finish/$', views.finish_production, name="finish_production"),
    url(r'^Order/(?P<order_id>[0-9]+)/Delete/$', views.delete_order, name="delete_order"),
    url(r'^Order/(?P<order_id>[0-9]+)/Report/$', views.detailed_report, name="detailed_report"),
    url(r'^Report/$', views.production_report, name="production_report"),


    ]