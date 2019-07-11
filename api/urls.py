# -*- coding: utf-8 -*-
__author__ = 'cty'
__date__ = '2019/7/11 19:13'
from Tapp.views import *
from django.urls import re_path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users',UserViewSet)


all_api = [

    re_path(r'',include(router.urls))
]

api_v1 = [re_path(r'',include(all_api))]

api_versions = [re_path(r'v1/',include(api_v1))]

urlpatterns = [re_path(r'api/',include(api_versions))]