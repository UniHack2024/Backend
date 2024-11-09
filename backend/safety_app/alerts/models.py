from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
class Warning(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField();
    location_lat = models.FloatField();
    location_lng = models.FloatField();
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class CivicReport(models.Model):
    warning = models.ForeignKey(Category, on_delete = models.CASCADE)
    report_description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add = True)
