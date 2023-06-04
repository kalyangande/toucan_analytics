from django.urls import path
from .views import *
from analytics import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('data/', views.DataView.as_view(), name='data'),
    path('analytics/',Analytics.as_view()),
    path('',index),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]