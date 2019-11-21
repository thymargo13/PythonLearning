from .models import Company
from rest_framework import viewsets
from .serializers import CompanySerializer


class CompanyView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

