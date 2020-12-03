from django.shortcuts import render
from .models import Test, UserInfo, Pet, PostLost, LostComment, PostFound, FoundComment
from .serializers import TestSerializer, UserInfoSerializer, PetSerializer, PostLostSerializer, LostCommentSerializer
from .serializers import PostFoundSerializer, FoundCommentSerializer
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

# pet 정보 가져오기
class GetPetAPIView(APIView):
    def get(self, request, user_id, name):
        serializer = PetSerializer(Pet.objects.filter(user_id=user_id, name = name), many=True)
        return Response(serializer.data)

# pet_list 정보 가져오기
class GetPetListAPIView(APIView):
    def get(self, request, user_id):
        serializer = PetSerializer(Pet.objects.filter(user_id=user_id), many=True)
        return Response(serializer.data)

# lost 글 쓰기
class WritePostLostViewSet(viewsets.ModelViewSet):
    serializer_class = PostLostSerializer
    queryset = PostLost.objects.all()

# lost 목록
class LostListAPIView(APIView):
    def get(self, request):
        serializer = PostLostSerializer(PostLost.objects.all().order_by("-post_id"), many=True)
        return Response(serializer.data)

# my lost 목록
class MyLostListAPIView(APIView):
    def get(self, request, user_id):
        serializer = PostLostSerializer(PostLost.objects.filter(user_id=user_id).order_by("-post_id"), many=True)
        return Response(serializer.data)

# lost 댓글 받아오기
class LostCommentAPIView(APIView):
    def get(self, request, post_id):
        serializer = LostCommentSerializer(LostComment.objects.filter(post_id=post_id).order_by("reg_time"), many=True)
        return Response(serializer.data)

# lost 댓글 작성
class WriteLostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = LostCommentSerializer
    queryset = LostComment.objects.all()

# found
# found 글 쓰기
class WritePostFoundViewSet(viewsets.ModelViewSet):
    serializer_class = PostFoundSerializer
    queryset = PostFound.objects.all()


# found 목록
class FoundListAPIView(APIView):
    def get(self, request):
        serializer = PostFoundSerializer(PostFound.objects.all().order_by("-post_id"), many=True)
        return Response(serializer.data)


# my lost 목록
class MyFoundListAPIView(APIView):
    def get(self, request, user_id):
        serializer = PostFoundSerializer(PostFound.objects.filter(user_id=user_id).order_by("-post_id"), many=True)
        return Response(serializer.data)


# lost 댓글 받아오기
class FoundCommentAPIView(APIView):
    def get(self, request, post_id):
        serializer = FoundCommentSerializer(FoundComment.objects.filter(post_id=post_id).order_by("reg_time"), many=True)
        return Response(serializer.data)


# lost 댓글 작성
class WriteFoundCommentViewSet(viewsets.ModelViewSet):
    serializer_class = FoundCommentSerializer
    queryset = FoundComment.objects.all()