from django.urls import path
from .views import SingleBrandView, SingleClothesView, SinglePriceView

app_name = "template_app"
# app_name will help us do a reverse look-up latter.
urlpatterns = [

    path('brand/<int:pk>', SingleBrandView.as_view()),
    path('clothes/<int:pk>', SingleClothesView.as_view()),
    path('price/<int:pk>', SinglePriceView.as_view()),
]