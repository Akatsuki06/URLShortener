from rest_framework import serializers
from basicapp import models
from django.utils import timezone

from basicapp.shortener_algo import algo

from urllib.parse import urlparse
BASE_URL='http://su06.herokuapp.com/'

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Link
        fields=('targetURL',)
        extra_kwargs = {'shortenURL':{'write_only':True},'created_date':{'write_only':True}}
