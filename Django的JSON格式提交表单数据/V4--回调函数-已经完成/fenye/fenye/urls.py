#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
import ff.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^json/$',ff.views.json,name='json'),
]
