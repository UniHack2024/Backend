from django.shortcuts import render
from rest_framework import viewsets
from .models import Warning, Category, CivicReport
from .serializers import WarningSerializer, CategorySerializer, CivicReportSerializer
# Create your views here.

class WarningViewSet(viewsets.ModelViewSet):
    queryset = Warning.objects.all()
    serializer_class = WarningSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CivicReportViewSet(viewsets.ModelViewSet):
    queryset = CivicReport.objects.all()
    serializer_class = CivicReportSerializer

