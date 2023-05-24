from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

import csv


# Create your views here.
@csrf_exempt
def analytics(request):
    
    if request.method == "GET":
        file = open('/home/gopikrishna/Taigo/analytics_env/toucan_analytics/Data/data_for_database.csv',mode='r')
        data = csv.reader(file)
        dL = list(data)
        dataList = dL[1:]
        for row in dataList:
            customerid = row[1]
            category = row[2]
            modeOfPayment = row[3]
            amount = row[4]
            date = row[5]
            break

        dictt = {
            
            "customerid" : customerid,
            "category" : category,
            "mode" : modeOfPayment,
            "amount" : amount,
            "date" : date
        }
        file.close()
        return JsonResponse(dictt)
    
    return HttpResponse("wow")

def index(request):
    return HttpResponse("index")
