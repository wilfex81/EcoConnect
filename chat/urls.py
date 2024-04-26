from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:room_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:room_id>/send_message/', views.send_message, name='send_message'),
    path('chat/<int:room_id>/message_history/', views.message_history, name='message_history'),
    path('chat/<int:room_id>/send_community_reply/', views.send_community_reply, name='send_community_reply'),
    path('chat/<int:room_id>/community_message_history/', views.community_message_history, name='community_message_history'),
    path('community-chat/', views.community_chat, name='community_chat'),
]
