from django.conf.urls import url
from find import views

urlpatterns = [
    url(r'^workflow_list/$', views.workflow_list, name='workflow_list'),
    url(r'^workflow_list/(?P<category_slug>[\w\-]+)/$', views.workflow_list, name='workflow_list'),
    url(r'^workflow_detail/(?P<id>[\w\-]+)/(?P<slug>[\w\-]+)/$', views.workflow_detail, name='workflow_detail'),
]