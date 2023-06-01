from django.urls import path
from .views import *
from analytics import views
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('analytics/',analytics),
    path('',index),
]