from rest_framework import serializers
from .models import News, Stocks

base_url = "http://127.0.0.1:8000"

class NewsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return base_url + obj.get_absolute_url()

    class Meta:
        model = News
        fields = "__all__"


class StocksSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return base_url + obj.get_absolute_url()

    class Meta:
        model = Stocks
        fields = "__all__"
