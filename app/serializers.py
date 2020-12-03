from rest_framework import serializers
from .models import Test, UserInfo, Pet, PostLost, LostComment

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

class PostLostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLost
        fields = "__all__"

class LostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostComment
        fields = "__all__"