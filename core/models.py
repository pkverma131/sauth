# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.

STATUS_CHOICES=(
            (1,'Registered'),
            (2, 'Verified'),
            (3, 'Tampered'),
            (4, 'Tampered WLC'),
            )

class Credential(models.Model):
    asset_code = models.CharField(verbose_name='Asset ID',max_length=32,default='')
    scan_time = models.DateTimeField(verbose_name='Scan Time', default=datetime.datetime.now)
    d1 = models.CharField(max_length=8,default='0.0')
    d2 = models.CharField(max_length=8,default='0.0')
    d3 = models.CharField(max_length=8,default='0.0')
    h1 = models.CharField(max_length=8,default='0.0')
    h2 = models.CharField(max_length=8,default='0.0')
    h3 = models.CharField(max_length=8,default='0.0')
    cp = models.CharField(max_length=8,default='0.0')
    fc = models.CharField(max_length=8,default='0.0')

    class Meta:
       abstract=True

class Verification(Credential):
    status=models.IntegerField(verbose_name='Staus',choices=STATUS_CHOICES)
    operator=models.CharField(verbose_name='Operator',max_length=32,default='')
    geo_location=models.CharField(verbose_name='Geo Point',max_length=32,default='0.0|0.0')
    street = models.CharField(verbose_name='Address', max_length=32, default='')
    locality = models.CharField(verbose_name='locality',max_length=128, default='')
    city = models.CharField(verbose_name='city',max_length=32,default='')
    state=models.CharField(verbose_name='state',max_length=32,default='')
    postal_code = models.CharField(verbose_name = 'Postal Code', max_length = 16, default = '')
    country=models.CharField(verbose_name='country', max_length = 32, default='')
    mobile = models.CharField(verbose_name = 'mobile', max_length = 16, default='')
    scan_remark = models.CharField(verbose_name='Scan Remark', max_length = 100, default= 'Not Provided')
    bit_mask = models.CharField(verbose_name= 'Bit Mask', max_length = 64, null = True, blank = True, default = '')
    email_id = models.CharField(verbose_name = 'Email Id', max_length = 64, null = True, blank = True, default = '')
    image = models.FileField(upload_to= 'media/documents/')


class Registration(Credential):
    location = models.CharField(verbose_name='location', max_length = 100, default= '')
    product_details = models.CharField(verbose_name = 'Product details', max_length = 100, null = True, blank = True, default= '')
    active=models.BooleanField(verbose_name='Active',default=True)

    def get_credentials(self):
    	return 'scan_time=%s-d1=%s-d2=%s-d3=%s-pd=%s'%(self.scan_time,self.d1,self.d2,self.d3,self.product_details)
