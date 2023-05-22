from django.urls import path
from .views import *

urlpatterns = [
    path('frequent-mode-of-payments',frequent_mode_of_payments),
    path('payments-per-interval',payments_per_interval),
    path('emi-payments',emi_payments),
    path('spending-sectors',spending_sectors)
]