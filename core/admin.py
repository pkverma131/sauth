# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Credential, Verification

class VerificationAdmin(admin.ModelAdmin):
	list_display = ('asset_code','status','scan_time','city','operator','mobile')
	list_filter = ('status','state')
	search_fields = ('asset_code','mobile')
	ordering =  ('-scan_time',)

admin.site.register(Verification,VerificationAdmin)

# Register your models here.
