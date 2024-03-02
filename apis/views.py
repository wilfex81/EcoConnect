from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework import generics, status
from rest_framework.response import Response
from oauth2_provider.models import AccessToken
from oauth2_provider.settings import oauth2_settings
from django.contrib.auth.models import User
from .models import (Notification, UserProfile, Post, Project, Event,
                     Community, Membership, Comment, Like)
from .serializers import (UserProfileSerializer, PostSerializer, ProjectSerializer,
                          EventSerializer, CommunitySerializer,
                          MembershipSerializer, CommentSerializer,
                          LikeSerializer, UserSerializer)


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        url, headers, body, status_code = oauth2_settings.OAUTH2_BACKEND.create_token_response(request)
        return Response(body, status=status_code, headers=headers)

class UserProfileListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CommunityListCreate(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class MembershipListCreate(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeListCreate(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    

