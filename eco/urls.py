from django.urls import path
from .views import (user_login, home, register, get_projects,
                    get_events, get_community, join_community, participate_in_event,
                    participate_in_project, cancel_event_participation, cancel_project_participation, 
                    register_user, cancel_community_mebership,add_event,edit_event,event_details
                    )

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login_submit'),
    path('register/', register, name='registration'),
    path('registration/', register_user, name='registration_submit'),
    path('projects/', get_projects, name='projects'),
    path('participate-in-project/<int:project_id>/',
         participate_in_project, name='participate_in_project'),
    path('cancel_participation-in-project/<int:project_id>/',
         cancel_project_participation, name='cancel_project_participation'),
    path("events/", get_events, name='events'),
    path('participate-in-event/<int:event_id>/',
         participate_in_event, name='participate_in_event'),
     path("add_event/", add_event, name='add_event'),
    path('events/<int:event_id>/details/', event_details, name='event_details'),
    path('events/<int:event_id>/edit/', edit_event, name='edit_event'),
    path('cancel_participation-in-event/<int:event_id>/',
         cancel_event_participation, name='cancel_event_participation'),
    path("communities/", get_community, name='communities'),
    path('join-community/<int:community_id>/',
         join_community, name='join_community'),
    path('cancel_community-membership/<int:community_id>/',
         cancel_community_mebership, name='cancel_membership'),
    
]
