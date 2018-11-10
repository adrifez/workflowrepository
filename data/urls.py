from django.conf.urls import url
from data import views

urlpatterns = [
    url(r'^base/$', views.base, name='base'),
]