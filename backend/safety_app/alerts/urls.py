from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, WarningViewSet, CivicReportViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'alerts', WarningViewSet)
router.register(r'civicreports', CivicReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
