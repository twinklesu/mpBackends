from django.shortcuts import render
from .models import Test
from .serializers import TestSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class TestAPIView(APIView):
    def get(self, request):
        serializer = TestSerializer(Test.objects.all(), many=True)
        return Response(serializer.data)