from django.shortcuts import render
from .models import Test
from .serializers import TestSerializer
from rest_framework import viewsets, permissions

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer