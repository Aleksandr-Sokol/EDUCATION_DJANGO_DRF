from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Brand, Price, Clothes, RequestJournal
from .serializers import BrandListSerializer, PriceListSerializer, ClothesListSerializer, RequestJournalSerializer


# Серилизаторы для /id
class SingleBrandView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class SingleClothesView(RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializer


class SinglePriceView(RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceListSerializer


# Серилизаторы для коллекции
class BrandView(ListCreateAPIView):
    """
    perform_create - действие после создания
    Если поле country пустое, то для бренда указываться country=china
    """
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

    def perform_create(self, serializer):
        country = self.request.data.get('country', '')
        if not country:
            return serializer.save(country='china')
        return serializer.save()


class ClothesView(ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializer


class PriceView(ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceListSerializer


class RequestJournalView(APIView):
    """
    При использовании данного подхода необходимо вручную написать все доступные методы
    """
    def get(self, request):
        request_journal = RequestJournal.objects.all()
        serializer = RequestJournalSerializer(request_journal, many=True)
        return Response({"articles": serializer.data})
