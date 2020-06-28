from django.urls import path, include
from .views.stockView import StockView

urlpatterns = [
    path('stock/<int:pk>', StockView.show, name='stock_detail'),
    path('company/<int:pk>/stocks', StockView.all, name='company_stocks'),
    path('stock/<int:pk>/predict', StockView.predict, name='stock_predict')
]