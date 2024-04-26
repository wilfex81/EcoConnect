from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ChatRoom, Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = room.messages.all().order_by('timestamp')
    return render(request, 'chat/chat_room.html', {'room': room, 'messages': messages})

@login_required
def send_message(request, room_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            room = get_object_or_404(ChatRoom, id=room_id)
            message = Message.objects.create(room=room, user=request.user, content=content)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def message_history(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = room.messages.all().order_by('timestamp')
    message_data = [{'user': msg.user.username, 'content': msg.content, 'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for msg in messages]
    return JsonResponse({'messages': message_data})


@login_required
def send_community_reply(request, room_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            room = get_object_or_404(ChatRoom, id=room_id)
            message = Message.objects.create(room=room, user=request.user, content=content)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def community_message_history(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    messages = room.messages.all().order_by('timestamp')
    message_data = [{'user': msg.user.username, 'content': msg.content, 'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for msg in messages]
    return JsonResponse({'messages': message_data})


@login_required
def community_chat(request):
    room_name = "Community Chat"
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = room.messages.all().order_by('timestamp')
    return render(request, 'chat/community_chat.html', {'room': room, 'messages': messages})