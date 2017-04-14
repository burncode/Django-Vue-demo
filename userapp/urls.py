# -*- coding: utf8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^user_info$', views.get_user_info),
    url(r'^github_file_explorer$', views.github_file_explorer),
]
