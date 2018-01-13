from django.db import models

from django.utils import timezone
from urllib.parse import urlparse
# Create your models here.
class Link(models.Model):
    linkid = models.AutoField(primary_key = True)
    created_date=models.DateTimeField(blank=True, default=timezone.now)
    shortenURL=models.CharField(max_length=500,unique=True)
    targetURL=models.CharField(max_length=500)

    def clean(self):
        targetURL=self.targetURL.lower()
        if urlparse(targetURL).scheme=='':
            targetURL='http://'+targetURL
        return targetURL
