from ..models import Stock
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.stockSerializer import StockSerializer

# Create your views here.

class StockView(object):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    @api_view(['GET'])
    def show(request, pk): 
        try:
            stock = Stock.objects.get(id=pk)
            serializer = StockSerializer(stock)
            return Response(serializer.data)
        except Stock.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
