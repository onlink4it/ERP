from django.conf.urls import url,static
from . import views

app_name = 'BRANCHES'

urlpatterns = [
    url(r'Branches/^$',views.create_branch,name="branches"),
    url(r'Branches//(?P<link_id>[0-9]+)/Delete/$',views.delete_branch,name="delete_branch"),
    url(r'Branches/Choose/$',views.choose_branch,name="choose_branch"),
    ]