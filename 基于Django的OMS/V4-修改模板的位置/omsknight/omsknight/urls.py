#coding:utf8

from django.conf.urls import include, url
from django.contrib import admin
from deploy.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ttt/$',ttt,name="ttt"),
#    url(r'^deploy/remote_execution/$', remote_execution, name='remote_execution'),  # 执行远程命令
    url(r'^exe/$',exe_test),    ##原始的
]
