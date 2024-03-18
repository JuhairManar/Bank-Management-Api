from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('banks/',BankAPIView.as_view(),name='banks'),
    path('banks/<int:pk>',BankDetailAPIView.as_view(),name='bank-details'),
    path('branches/',BranchesAPIView.as_view(),name='branches'),
    path('branches/<int:pk>',BranchDetailAPIView.as_view(),name='branch-details'),
]