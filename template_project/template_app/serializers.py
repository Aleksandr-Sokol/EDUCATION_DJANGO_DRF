from .models import Brand, Price, Clothes
from rest_framework import serializers
from .debug.query import query_debugger
from django.db.models import Avg


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['title', 'country']


class ClothesListSerializer(serializers.ModelSerializer):
    """
    Переоределен метод create, что бы автоматически создавать и привязывать бренд к одежде
    brand=BrandListSerializer(read_only=True) используется только для get запроса
    brand_data=serializers.JSONField(write_only=True) используется только для post запроса. В get запросе не применяется
    """
    brand = BrandListSerializer(read_only=True)
    brand_data = serializers.JSONField(write_only=True)

    class Meta:
        model = Clothes
        fields = ['title', 'size', 'brand', 'brand_data']

    def create(self, validated_data):
        brand_data: dict = validated_data.pop('brand_data')
        brand, is_created = Brand.objects.get_or_create(**brand_data)
        clothes = Clothes(**validated_data)
        clothes.brand = brand
        clothes.save()
        return clothes


class PriceListSerializer(serializers.ModelSerializer):
    """
    middle_price при ответе автоматически вычисляется средняя цена
    """
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


class RequestJournalSerializer(serializers.Serializer):
    """
    Устаревший метод серилизатора, но возможно более быстрый
    """
    date = serializers.DateField()
    request = serializers.CharField(max_length=1000)
    response_code = serializers.IntegerField()
    response_message = serializers.CharField(max_length=1000)
