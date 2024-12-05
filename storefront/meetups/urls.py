from django.urls import path
from . import views

urlpatterns = [
    path("meetups/", views.index), # domain.com/meetups,
    path('meetups/<slug:meetup_slug>', views.meetup_details) #domain.com/meetups/<dynamic-path-segment>
]