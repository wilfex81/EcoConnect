from django.urls import path
from .views import (
    UserProfileListCreate, UserProfileDetail,
    PostListCreate, PostDetail,
    ProjectListCreate, ProjectDetail,
    EventListCreate, EventDetail,
    CommunityListCreate, CommunityDetail,
    MembershipListCreate, MembershipDetail,
    CommentListCreate, CommentDetail,
    LikeListCreate, LikeDetail,UserRegistrationAPIView,UserLoginAPIView
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('userprofiles/', UserProfileListCreate.as_view(), name='userprofile-list-create'),
    path('userprofiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('communities/', CommunityListCreate.as_view(), name='community-list-create'),
    path('communities/<int:pk>/', CommunityDetail.as_view(), name='community-detail'),
    path('memberships/', MembershipListCreate.as_view(), name='membership-list-create'),
    path('memberships/<int:pk>/', MembershipDetail.as_view(), name='membership-detail'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('likes/', LikeListCreate.as_view(), name='like-list-create'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),
]
