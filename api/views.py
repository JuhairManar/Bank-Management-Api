from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

class BankAPIView(generics.ListCreateAPIView):
    queryset=Bank.objects.all()
    serializer_class=BankSerializer
    
class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bank.objects.all()
    serializer_class=BankSerializer
    
class BranchesAPIView(generics.ListCreateAPIView):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer
    
class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer
