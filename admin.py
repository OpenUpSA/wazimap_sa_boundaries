# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.shortcuts import render
from django.conf.urls import url


from .models import Province

class ProvinceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Province, ProvinceAdmin)

