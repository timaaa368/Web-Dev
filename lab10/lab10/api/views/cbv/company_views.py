from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Company

from api.serializers import CompanySerializer, VacancySerializer


class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'

class CompanyVacanciesAPIView(APIView):
    def get(self, request, id):
        try:
            company = Company.objects.get(id=id)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

        vacancies = company.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


