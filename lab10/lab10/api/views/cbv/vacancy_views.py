from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Vacancy;
from api.serializers import CompanySerializer, SimpleVacancySerializer, VacancySerializer

class VacancyListCreateAPIView(ListCreateAPIView):
  queryset = Vacancy.objects.all()
  serializer_class = VacancySerializer


class VacancyDetailAPIView(APIView):
  def get_object(self, id):
    try:
      return Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
      return None

  def get(self, request, id):
    vacancy = self.get_object(id)
    if not vacancy:
      return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = SimpleVacancySerializer(vacancy)
    return Response(serializer.data)

  def put(self, request, id):
    vacancy = self.get_object(id)
    if not vacancy:
      return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = SimpleVacancySerializer(vacancy, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    vacancy = self.get_object(id)
    if not vacancy:
      return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)
    vacancy.delete()
    return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)


class TopTenVacanciesAPIView(APIView):
  def get(self, request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
