from django.http import JsonResponse

from .models import Company, Vacancy


def company_list(request):
    companies = list(Company.objects.values())
    return JsonResponse(companies, safe=False)


def company_detail(request, id):
  companies = Company.objects.filter(id=id).values()
  return JsonResponse(list(companies), safe=False)


def company_vacancies(request, id):
  products = list(Vacancy.objects.filter(company_id=id).values())
  return JsonResponse(products, safe=False)


def vacancy_list(request):
  vacancies = list(Vacancy.objects.values())
  return JsonResponse(vacancies, safe=False)


def vacancy_detail(request, id):
  vacancies = Vacancy.objects.filter(id=id).values()
  return JsonResponse(list(vacancies), safe=False)


def vacancy_top_ten(request):
  vacancies = Vacancy.objects.all().order_by('-salary')[:10].values()
  return JsonResponse(list(vacancies), safe=False)
