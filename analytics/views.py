from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import CustomerData,EMIData
import csv
from django.db import models
from django.db.models import Count,Sum,Max


# Create your views here.
def table(request):
    unique_customers=CustomerData.objects.values('customer_Id').annotate(frequent_modes_of_transanction=Max('mode_of_payments'))
    # For TABLE
    customer = []
    values = []
    for item in unique_customers:
        customer.append(item['customer_Id'])
        values.append(item['frequent_modes_of_transanction'])

    response_data = {
            "customer" : customer,
            "values" :values
        }
    # Return the JSON response
    return JsonResponse(response_data)
def bar(request):
    result=CustomerData.objects.values('mode_of_payments').annotate(total_amount=Sum('amount_spent'))
    # For BAR GRAPH
    mode =[]
    amount=[]
    for item in result:
        mode.append(item['mode_of_payments'])
        amount.append(item['total_amount'])
    response_data = {
            "mode" : mode,
            "amount" : amount,
        }
    
    # Return the JSON response
    return JsonResponse(response_data)

def pie(requests):
    grouped_data = CustomerData.objects.values('category').annotate(sum_field=Sum('amount_spent'))

# For PIE CHART
    labels = []
    total = []
    sizes = []
    for entry in grouped_data:
        labels.append(entry['category']) 
        total.append(entry['sum_field'])

    sum_1 = sum(total)

    for i in range(len(total)):
        per = (total[i]/sum_1)*100
        sizes.append(per)

    response_data = {
            "labels" : labels,
            "sizes" : sizes,
        }
    return JsonResponse(response_data)

def emi(request):
    EMI=EMIData.objects.values('EMI_paid_on_time').annotate(total_customers=Count('customer_Id')).order_by()
    inTime =[]
    total=[]
    for item in EMI:
        inTime.append(item['EMI_paid_on_time'])
        total.append(item['total_customers'])
    response_data = {
            "in_time" : inTime,
            "total" : total,
        }
    
    # Return the JSON response
    return JsonResponse(response_data)

@csrf_exempt
def analytics(request):
    if request.method == "GET":
        type = request.GET.get('type')
        if type == "table":
            response = table(request)
            return response
        elif type == "bar":
            response = bar(request)
            return response
        elif type == "pie":
            response = pie(request)
            return response
        elif type == "emi":
            response = emi(request)
            return response
    else:
        return HttpResponse("WOW")
    

def index(request):
    return HttpResponse("index")




