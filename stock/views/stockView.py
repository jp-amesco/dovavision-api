import datetime
import pandas as pd
import tensorflow as tf
from ..models import Stock
from rest_framework import status
from .handleData import HandlerData
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dateutil.relativedelta import relativedelta
from ..serializers.stockSerializer import StockSerializer


class StockView(object):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    @api_view(['GET'])
    def show(request, pk): 
        try:
            stock = Stock.objects.get(id=pk)
            serializer = StockSerializer(stock)
            return Response(serializer.data)
        except Stock.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    def all(request, pk):
        stock = Stock.objects.filter(company_id=pk)
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def predict(request, pk):
        stock = Stock.objects.get(id=pk)
        end = datetime.datetime.now()
        start = end + relativedelta(months=-2)
        data = HandlerData.get_data(stock.api_name, start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
        data['Labels'] = HandlerData.get_labels(data).astype(int)
        data_predict = HandlerData.get_inputs(data['Labels'])
        model_move = tf.keras.models.load_model('/home/joao/Desktop/dovavisionApi/dovavision-api/stock/models/predict_move4_value.h5')
        move = int(model_move.predict(pd.DataFrame(data_predict).transpose()).flatten()[0])

        data_predict_price = data.tail(n=1).reset_index()
        data_predict_price.pop('Volume')
        data_predict_price.pop('Adj Close')
        data_predict_price.pop('High')
        data_predict_price.pop('Low')
        data_predict_price.pop('Close')
        data_predict_price['Date'] = HandlerData.format_date(data_predict_price['Date'])
        data_predict_price['Date'] = data_predict_price['Date'] / 183.6843760344257
        data_predict_price['Open'] = data_predict_price['Open'] / 16.945615799363257
        data_predict_price['Move'] = move
        data_predict_price = pd.DataFrame({
            'Date': data_predict_price['Date'], 
            'Open': data_predict_price['Open'],
            'Move': move
        })
        model_price = tf.keras.models.load_model('/home/joao/Desktop/dovavisionApi/dovavision-api/stock/models/predict10_value.h5')
        future_price = model_price.predict(data_predict_price).flatten()
        content = {'move': move, 'price': future_price[0]}
        return Response(content)