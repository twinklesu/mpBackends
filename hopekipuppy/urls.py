"""hopekipuppy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'join', views.JoinViewSet)
router.register(r'reg-pet', views.RegPetViewSet)
router.register(r'write-post-lost', views.WritePostLostViewSet)
router.register(r'write-comment-lost', views.WriteLostCommentViewSet)
router.register(r'write-post-found', views.WritePostFoundViewSet)
router.register(r'write-comment-found', views.WriteFoundCommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/', views.TestAPIView.as_view()),
    path('validate-id/<user_id>/', views.ValidateIdAPIView.as_view()),
    path('validate-tel/<user_tel>/', views.ValidateTelAPIView.as_view()),
    path('login/<user_id>/', views.LoginAPIView.as_view()),
    path('get-pet/<user_id>/<name>/', views.GetPetAPIView.as_view()),
    path('get-pet-list/<user_id>/', views.GetPetListAPIView.as_view()),
    path('get-lost-list/', views.LostListAPIView.as_view()),
    path('my-lost-list/<user_id>/', views.MyLostListAPIView.as_view()),
    path('get-lost-comment/<post_id>/', views.LostCommentAPIView.as_view()),

    path('get-found-list/', views.FoundListAPIView.as_view()),
    path('my-found-list/<user_id>/', views.MyFoundListAPIView.as_view()),
    path('get-found-comment/<post_id>/', views.FoundCommentAPIView.as_view()),

    path('test-function/', views.TestFunctionAPIView.as_view()),
]
