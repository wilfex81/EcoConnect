from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm,EventForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from apis.models import Community, CommunityMembership, EventsParticipants, Project, Event, ProjectParticipant


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/registration.html')
    
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def get_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'projects.html', context)


def participate_in_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=project_id)
        user = request.user
        membership, participating = ProjectParticipant.objects.get_or_create(
            user=request.user, project=project
        )
        if participating:
            return JsonResponse({'message': 'Participation recorded successfully.😊'})
        else:
            return JsonResponse({'message': 'Already participating in this project.😁'}, status=400)

def cancel_event_participation(request, event_id):
    user = request.user
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return JsonResponse({'message': 'Event not found.'}, status=404)
    
    try:
        participation = EventsParticipants.objects.get(user=user, event=event)
    except EventsParticipants.DoesNotExist:
        return JsonResponse ({'message': 'You are not participating in this event.😭'},status=400)
    
    participation.delete()
    return JsonResponse({'message': 'Participation canceled successfully.😊'})
    


def get_events(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }

    return render(request, 'events.html', context)


def participate_in_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        user = request.user
        membership, participating = EventsParticipants.objects.get_or_create(
            user=request.user, event=event
        )
        if participating:
            return JsonResponse({'message': 'Participation recorded successfully.😊'})
        else:
            return JsonResponse({'message': 'Already participating in this event.😁'}, status=400)
        
        
def cancel_project_participation(request, project_id):
    user = request.user
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return JsonResponse({'message': 'Project not found.'}, status=404)
    
    try:
        participation = ProjectParticipant.objects.get(user=user, project=project)
    except ProjectParticipant.DoesNotExist:
        return JsonResponse ({'message': 'You are not participating in this project.😭'},status=400)
    
    participation.delete()
    return JsonResponse({'message': 'Participation canceled successfully.😊'})
    
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'events.html', {'form': form})

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    data = {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'location': event.location,
        'date': event.date,
        'time': event.time
    }
    return JsonResponse(data)


def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'PUT':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Event updated successfully.'})
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)
    else:
        # Pass event ID in the context to be used in the template
        context = {'form': EventForm(instance=event), 'event_id': event_id}
        return render(request, 'events.html', context)


def delete_event(request, event_id):
    # Retrieve the event object from the database
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events')

    return render(request, 'events.html', {'event': event})

def get_community(request):
    communities = Community.objects.all()
    context = {
        'communities': communities,
    }
    return render(request, 'communities.html', context)


def join_community(request, community_id):
    if request.method == 'POST':
        community = get_object_or_404(Community, pk=community_id)
        user = request.user
        membership, created = CommunityMembership.objects.get_or_create(
            user=request.user, community=community)
        if created:
            return JsonResponse({'message': 'Joined community successfully.😊'})
        else:
            return JsonResponse({'message': 'Already a member of this community.😁'}, status=400)

def cancel_community_mebership(request, community_id):
    user = request.user
    try:
        community = Community.objects.get(pk=community_id)
    except Community.DoesNotExist:
        return JsonResponse({'message': 'Community not found.'}, status=404)
    
    try:
        membership = CommunityMembership.objects.get(user=user, community=community)
    except CommunityMembership.DoesNotExist:
        return JsonResponse ({'message': 'You are not a member of this community.😭'},status=400)
    
    membership.delete()
    return JsonResponse({'message': 'Community membership canceled successfully.😊'})
      