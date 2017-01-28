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
]
