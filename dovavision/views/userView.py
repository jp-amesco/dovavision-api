from ..models import User
from stock.models import Stock
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from ..serializers.userSerializer import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @api_view(['POST'])
    @permission_classes((AllowAny,))
    def user_create(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PATCH', 'GET'])
    def show_or_update(request, pk): 
        user = User.objects.get(id=pk)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        if request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    def favourite_stock(request):
        user = request.user
        stock_id = request.data['stock_id']
        try:
            stock = Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        response = user.stock_set.add(stock)
        return Response(response, status=status.HTTP_200_OK)