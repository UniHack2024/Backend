from rest_framework import serializers
from .models import Warning, Category, CivicReport

class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warning
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CivicReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CivicReport
        fields = '__all__'