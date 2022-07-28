from django.urls import path
from . import views

urlpatterns = [
    path('btc', views.BTCDonation, name='BTCDonation'),
    path('eth', views.ETHDonation, name='ETHDonation'),
    path('usdt', views.USDTDonation, name='USDTDonation'),
]
