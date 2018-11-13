"""workflowrepository URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

from data import views as dataviews
from find import views as findviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/', include('data.urls')),
    url(r'^find/', include('find.urls')),
	url(r'^base/', dataviews.base, name='base'),
    url(r'^workflow_list/$', findviews.workflow_list, name='workflow_list'),
    url(r'^workflow_list/(?P<category_slug>[\w\-]+)/$', findviews.workflow_list, name='workflow_list'),
    url(r'^workflow_detail/(?P<id>[\w\-]+)/(?P<slug>[\w\-]+)/$', findviews.workflow_detail, name='workflow_detail'),
    url(r'^^workflow_search/(?P<name>[-\w]+)/$', findviews.workflow_search, name='workflow_search'),
    url(r'^workflow_search/$', views.workflow_search, name='workflow_search'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
