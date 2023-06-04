from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomerData,EMIData
from django.db.models import Count,Sum,Max


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def table(request,start_date,end_date):
    
    unique_customers=CustomerData.objects.filter(date__range=[start_date, end_date]).values('customer_Id').annotate(frequent_modes_of_transanction=Max('mode_of_payments'))
    customer = []
    values = []
    
    for item in unique_customers:
        customer.append(item['customer_Id'])
        values.append(item['frequent_modes_of_transanction'])

    response_data = {
            "customer" : customer,
            "values" :values
        }
    
    return response_data

def bar(request,start_date,end_date):
    
    mode_of_payments=CustomerData.objects.filter(date__range=[start_date, end_date]).values('mode_of_payments').annotate(total_amount=Sum('amount_spent'))
    mode =[]
    amount=[]
    
    for item in mode_of_payments:
        mode.append(item['mode_of_payments'])
        amount.append(item['total_amount'])
    
    response_data = {
            "mode" : mode,
            "amount" : amount,
        }
    
    return response_data

def pie(requests,start_date,end_date):
    
    grouped_data = CustomerData.objects.filter(date__range=[start_date, end_date]).values('category').annotate(sum_field=Sum('amount_spent'))

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
    
    return response_data

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
    
    return response_data

    

def index(request):
    return HttpResponse("index")



class DataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        try:
            token = request.META['HTTP_AUTHORIZATION'].split()[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            data = {"WOW":"WOW"}
            return Response(data)
        
        except Exception as e:
            return Response({'error': str(e)}, status=401)


class Analytics(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        try:
            res ={"WOW":"wow - 1"}
            Type = self.request.GET.get('type')
            start_date = self.request.GET.get("start_date")
            end_date = self.request.GET.get("end_date")
            if Type == "table":
                res = table(request,start_date,end_date)
            elif Type == "bar":
                res = bar(request,start_date,end_date)
            elif Type == "pie":
                res = pie(request,start_date,end_date)
            elif Type == "emi":
                res = emi(request)
            return JsonResponse(res)
            
        except Exception as e:
            return Response({'error': str(e)})