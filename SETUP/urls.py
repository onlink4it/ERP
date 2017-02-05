from django.conf.urls import url,static,include
from . import views

app_name = 'SETUP'

urlpatterns = [
    url(r'^$', views.setup_index, name='setup'),
    ]