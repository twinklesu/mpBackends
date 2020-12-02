from django.shortcuts import render
from .models import Test, UserInfo, Pet, PostLost
from .serializers import TestSerializer, UserInfoSerializer, PetSerializer, PostLostSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection

class TestAPIView(APIView):
    def get(self, request):
        serializer = TestSerializer(Test.objects.all(), many=True)
        return Response(serializer.data)

# id 중복 확인
class ValidateIdAPIView(APIView):
    def get(self, request, user_id):
        if UserInfo.objects.filter(user_id = user_id).exists():
            return Response(data={'message':False}) #이 id 이미 있다
        else:
            return Response(data={'message':True})

# 전화번호 중복 확인
class ValidateTelAPIView(APIView):
    def get(self, request, user_tel):
        if UserInfo.objects.filter(user_tel = user_tel).exists():
            return Response(data={'message':False}) #이미 가입된 전화번호 이미 있다
        else:
            return Response(data={'message':True})

# 회원가입
class JoinViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()

# 로그인
class LoginAPIView(APIView):
    def get(self, request, user_id):
        if UserInfo.objects.filter(user_id = user_id).exists():
            serializer = UserInfoSerializer(UserInfo.objects.filter(user_id = user_id), many=True)
            return Response(serializer.data)
        else:
            return Response(data=None)

# pet 정보 등록
class RegPetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

# lost 글 쓰기
class RegPetViewSet(viewsets.ModelViewSet):
    serializer_class = PostLostSerializer
    queryset = PostLost.objects.all()