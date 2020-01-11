from ..models import User, Company
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers.userSerializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @api_view(['POST'])
    def user_create(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
    def favourite_company(request):
        user = request.user
        company_id = request.data['id_company']
        company = Company.objects.get(id=company_id)
        response = user.company_set.add(company)
        return Response(response, status=status.HTTP_200_OK)