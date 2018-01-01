from rest_framework import serializers
from basicapp import models


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Link
        fields=('created_date','shortenURL','targetURL')
