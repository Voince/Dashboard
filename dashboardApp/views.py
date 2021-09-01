from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from dashboardApp.models import Quake
from dashboardApp.models import datapoint
from django.template.context import Context
import pandas as pd

# Create your views here.
def quake_dataset(request):
    quakes=serialize('json', Quake.objects.order_by("ID")[:1000])
    return HttpResponse(quakes, content_type='json')

def datapoint_dataset(request):
    _datapoint = serialize('json',datapoint.objects.order_by("ID")[:1000])
    
    # dg = []

    # for each in datapoint.objects.all():
    #     if (dg:Datapoint_Group == datapoint:Datapoint_Group)
    #         dg.append(each.Datapoint_Group)

    #     else 

    return HttpResponse(_datapoint, content_type='json')




def home(request):
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page'
        }
    )