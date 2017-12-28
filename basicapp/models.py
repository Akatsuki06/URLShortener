from django.db import models

from django.utils import timezone
# Create your models here.
class Link(models.Model):
    linkid=models.AutoField(primary_key=True)
    label=models.CharField(max_length=50,blank=True)
    created_date=models.DateTimeField(blank=True, default=timezone.now)
    shortenURL=models.CharField(max_length=10,unique=True)
    targetURL=models.CharField(max_length=500)
