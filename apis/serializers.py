from rest_framework import serializers
from .models import UserProfile, Post, Project, Event, Community, Membership, Comment, Like
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    participants = serializers.SerializerMethodField()
    creator = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_participants(self, obj):
        return [participant.username for participant in obj.participants.all()]

    def get_creator(self, obj):
        return obj.creator.username


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
