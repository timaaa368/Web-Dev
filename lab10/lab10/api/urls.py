from django.urls import path

from api.views.cbv.company_views import CompanyListCreateAPIView, CompanyDetailAPIView, CompanyVacanciesAPIView
from api.views.cbv.vacancy_views import VacancyListCreateAPIView, VacancyDetailAPIView, TopTenVacanciesAPIView
from .views.fbv import company_views, vacancy_views

# urlpatterns = [
#   path('companies/', company_views.company_list),
#   path('companies/<int:id>/', company_views.company_detail),
#   path('companies/<int:id>/vacancies/', company_views.company_vacancies),
#   path('vacancies/', vacancy_views.vacancy_list),
#   path('vacancies/<int:id>/', vacancy_views.vacancy_detail),
#   path('vacancies/top_ten/', vacancy_views.vacancy_top_ten)
# ]

urlpatterns = [
  path('companies/', CompanyListCreateAPIView.as_view()),
  path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
  path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view()),
  path('vacancies/', VacancyListCreateAPIView.as_view()),
  path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),
  path('vacancies/top_ten/', TopTenVacanciesAPIView.as_view()),
]
