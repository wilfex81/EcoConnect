from django.utils import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length = 100,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"Post by {self.user.username}"
    
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(default = datetime.datetime.now())
    end_date = models.DateField(default = datetime.datetime.now())
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    participants = models.ManyToManyField(User, related_name='joined_projects')

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user.username} - {self.community.name}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username}"   
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username}"
    
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.recipient} - {self.message}"