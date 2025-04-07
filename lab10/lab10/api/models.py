from django.db import models
from django.db.models import CASCADE


class Company(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  city = models.CharField(max_length=255)
  address = models.TextField()

class Vacancy(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  salary = models.FloatField()

  company = models.ForeignKey(Company, on_delete=CASCADE, related_name='vacancies')
