from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


@api_view(["GET", "POST"])
def company_list(request):
  if request.method == 'GET':
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def company_detail(request, id):
  try:
    company = Company.objects.get(id=id)
  except Company.DoesNotExist:
    return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = CompanySerializer(company)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = CompanySerializer(company, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    company.delete()
    return Response({"deleted": True}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def company_vacancies(request, id):
  try:
    company = Company.objects.get(id=id)
  except Company.DoesNotExist:
    return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)
  vacancies = company.vacancies.all()
  serializer = VacancySerializer(vacancies, many=True)
  return Response(serializer.data)


