from ..models import Company
from rest_framework.decorators import api_view
from ..serializers.companySerializer import CompanySerializer 
from rest_framework.response import Response

class CompanyViewSet(object):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @api_view(['GET'])
    def show(request, pk):
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
