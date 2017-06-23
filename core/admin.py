# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Credential, Verification, Registration

class VerificationAdmin(admin.ModelAdmin):
	list_display = ('asset_code','status','scan_time','city','operator','mobile')
	list_filter = ('status','state')
	search_fields = ('asset_code','mobile')
	ordering =  ('-scan_time',)

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('asset_code','scan_time','location','product_details','active')
	list_filter = ('location',)
	search_fields = ('asset_code',)
	ordering =  ('-scan_time',)
	actions = ['release']

	def release(self, request, queryset):
		rows_updated = queryset.update(active=False)
		if rows_updated == 1:
			message_bit = "1 record"
		else:
			message_bit = "%s records" % rows_updated
		self.message_user(request, "%s successfully released." % message_bit)
	release.short_description = "Release selected assets"

admin.site.register(Verification,VerificationAdmin)
admin.site.register(Registration,RegistrationAdmin)

# Register your models here.
