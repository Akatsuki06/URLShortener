from django.db import models

from django.utils import timezone
# Create your models here.
class Link(models.Model):
    label=models.CharField(max_length=50,blank=True)
    created_date=models.DateTimeField(blank=True, default=timezone.now)
    shortURL=models.CharField(max_length=10,primary_key=True)
