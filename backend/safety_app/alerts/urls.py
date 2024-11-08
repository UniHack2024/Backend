from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarningViewSet, CategoryViewSet, CivicReportViewSet

router = DefaultRouter()
router.register(r'warnings', WarningViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'civicreports', CivicReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('warnings.urls')),  # Include your app's URLs here
]