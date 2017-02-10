from rest_framework import serializers
from .models import stalks


class stalkSerializer(serializers.ModelSerializer):

    class Meta:
        model=stalks
        fields=('ticker','open','close','volume')
