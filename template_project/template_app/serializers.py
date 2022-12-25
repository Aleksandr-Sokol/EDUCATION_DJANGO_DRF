from .models import Brand, Price, Clothes
from rest_framework import serializers
from .debug.query import query_debugger
from django.db.models import Avg


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['title', 'country']


class ClothesListSerializer(serializers.ModelSerializer):
    brand = BrandListSerializer()

    class Meta:
        model = Clothes
        fields = ['title', 'size', 'brand']


class PriceListSerializer(serializers.ModelSerializer):
    clothes = ClothesListSerializer()
    middle_price = serializers.SerializerMethodField()

    @query_debugger
    def get_middle_price(self, instance):
        """
        :param instance: модель Price
        :return: среднее значение цен для текущего вида одежды
        """
        prices: dict = Price.objects.values('value').filter(clothes=instance.clothes).aggregate(avg_res=Avg('value'))
        return prices.get('avg_res', 0)

    class Meta:
        model = Price
        fields = ['value', 'date', 'clothes', 'middle_price']
