#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Jeremy Low

"""dsa_signin_sheets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views

from signin_sheets import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^start/$', views.FirstRun.as_view(), name='start'),
    url(r'^event/list/$', views.EventListView.as_view(), name='event-list'),
    url(r'^event/new/$', views.EventCreateView.as_view(), name='event-create'),
    url(r'^event/(?P<pk>[0-9]+)/delete/$', views.EventDeleteView.as_view(), name='event-delete'),
    url(r'^event/(?P<pk>[0-9]+)/signin/$', views.EventSigninView.as_view(), name='event-signin'),
    url(r'^event/(?P<pk>[0-9]+)/participants/$', views.event_participants, name='event-participants'),
    url(r'^event/(?P<pk>[0-9]+)/export/$', views.event_to_csv, name='event-export'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetailView.as_view(), name='event-detail'),
]
