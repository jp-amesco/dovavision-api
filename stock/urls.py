from django.urls import path, include
from .views.stockView import StockView

urlpatterns = [
    path('stock/<int:pk>', StockView.show, name='stock_detail')
]