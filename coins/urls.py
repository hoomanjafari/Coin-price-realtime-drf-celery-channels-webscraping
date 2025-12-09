from django.urls import path
from .views import CoinsPriceView


app_name = 'coins'
urlpatterns = [
    path('', CoinsPriceView.as_view(), name='coins-detail'),
]
