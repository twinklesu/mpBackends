from django.shortcuts import render
from .models import Test
from .serializers import TestSerializer
from rest_framework import viewsets, permissions

class TestAPIView(APIView):
    def get(self, request):
        serializer = TestSerializer(Test.objects.all())
        return Response(serializer.data)