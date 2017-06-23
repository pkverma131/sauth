# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .forms import FetchForm
from core.models import Verification,Registration

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def fetch(request):
    data=''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FetchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            asset_code = form.cleaned_data['asset_code']
            robjs=Registration.objects.filter(asset_code=asset_code).order_by('-scan_time')
            if robjs.count()>0:
            	r=robjs[0]
            	data=r.get_credentials()
            else:
            	data='none'
    return render_to_response('raw.html', {'data': data})
