from django.conf.urls import url,static
from . import views

app_name = 'REPORTS'

urlpatterns = [
    url(r'^$',views.reports_index,name="reports"),
    url(r'^This/Day/$',views.this_day, name="this_day"),
    url(r'^This/Day/Detailed/$',views.this_month, name="this_day_detailed"),
    url(r'^This/Month/$',views.this_month, name="this_month"),
    url(r'^This/Month/$',views.this_month, name="this_month_detailed"),
    url(r'^This/Year/$',views.this_year, name="this_year"),
    url(r'^This/Year/$',views.this_year, name="this_year_detailed"),
    #url(r'^Year/(?P<year>[0-9]+)/Month/(?P<month>[0+9]+)/Day/(?P<day>[0+9]+)/',views.reports_index, name="custom_day"),
    #url(r'^Year/(?P<year>[0+9]+)/Month/(?P<month>[0+9]+)/',views.reports_index, name="custom_month"),
    #url(r'^Year/(?P<year>[0+9]+)/',views.reports_index, name="custom_year"),
    
   ]