from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=90, blank=False)
    country = models.CharField(max_length=90, blank=True)  # type: ignore

    class Meta:
        db_table = "brand"
        verbose_name = "бренд одежды"

    def __str__(self):  # отображения модели
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=90, blank=False)
    size = models.IntegerField(blank=False)
    brand = models.ForeignKey(
        Brand,
        verbose_name='Бренд',
        blank=True,
        null=True,
        related_name='brand',
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True


class Clothes(Product):

    class Meta:
        db_table = "clothes"
        verbose_name = "Одежда"

    def __str__(self):  # отображения модели
        return self.title


class Price(models.Model):
    value = models.FloatField(blank=False)
    date = models.DateField()
    clothes = models.ForeignKey(
        Clothes,
        verbose_name='Одежда',
        blank=True,
        null=True,
        related_name='clothes',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "price"
        verbose_name = "Цена на текущее время"

    def __str__(self):  # отображения модели
        return f'{self.value}'


class RequestJournal(models.Model):
    date = models.DateField(auto_now_add=True)
    request = models.CharField(max_length=1000)
    response_code = models.IntegerField(blank=True, null=True)
    request_method = models.CharField(max_length=5)

    class Meta:
        db_table = "request_journal"
        verbose_name = "Журнал запросов"

    def __str__(self):  # отображения модели
        return f'{self.request}'
