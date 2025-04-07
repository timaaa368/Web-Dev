from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from api.serializers import VacancySerializer
from api.models import Vacancy


@api_view(["GET", "POST"])
def vacancy_list(request):
  if request.method == "GET":
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)
  elif request.method == "POST":
    serializer = VacancySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def vacancy_detail(request, id):
  try:
    vacancy = Vacancy.objects.get(id=id)
  except Vacancy.DoesNotExist:
    return Response({"error:Vacancy not found"}, status=HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = VacancySerializer(vacancy)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = VacancySerializer(vacancy, request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    vacancy.delete()
    return Response({"deleted": True}, status=HTTP_204_NO_CONTENT)

@api_view(["GET"])
def vacancy_top_ten(request):
  vacancies = Vacancy.objects.order_by("-salary")[:10]
  serializer = VacancySerializer(vacancies, many=True)
  return Response(serializer.data)
