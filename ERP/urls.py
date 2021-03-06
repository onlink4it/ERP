from django.conf.urls import  include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'ERP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ERP/', include('BASE.urls')),
    url(r'^POS/',include('POS.urls')),
    url(r'^Delivery/',include('DELIVERY.urls')),
    url(r'^Purchases/', include('PURCHASES.urls')),
    url(r'^Reports/',include('REPORTS.urls')),
    url(r'^Manufacture/',include('MANUFACTURE.urls')),
    url(r'^SETUP/',include('SETUP.urls')),
]
