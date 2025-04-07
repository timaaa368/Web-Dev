from django.core.serializers import serialize
from django.test import TestCase
from rest_framework import serializers

from lab10.api.models import Company


# Create your tests here.

class Serializer(serializers.ModelSerializer):
    class Meta:
      model = Company
      fi
