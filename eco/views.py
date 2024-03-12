from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from apis.models import Project, Event


def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or the homepage
            # Update 'home' with the name of your homepage URL
            return redirect('home')
        else:
            # Display an error message if authentication fails
            messages.error(request, 'Invalid username or password.')
    # Render the login template with any error messages or a blank form
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form': form})
    if request.method == 'POST':
        form = RegistrationForm()
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            # Redirect to the login page after successful registration
            return redirect('home')
        return render(request, 'registration/registration.html', {'form': form})


def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'projects.html', context)

def events(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    
    return render(request,'events.html',context)

def community(request):
    pass