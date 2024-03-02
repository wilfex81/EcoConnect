from django.contrib import admin
from .models import (Comment, Community, Event, Like,
                    Membership, Post,UserProfile,Project)

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Event)
admin.site.register(Like)
admin.site.register(Membership)

