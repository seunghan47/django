from django.shortcuts import render
# from django.http import HttpResponse

# the path is relative to the teamplates directory already
def index(request):
    meetups = [
        { 'title': 'A first meetup', 
        'location': 'New York', 
        'slug': 'a-first-meetup'},
        { 'title': 'A second meetup', 
        'location': 'Paris', 
        'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': False,
        'meetups': meetups
    })


def meetup_details(request):
    selected_meetup = {
        'title' : 'A First Meetup',
        'description': 'this is first meetup!'
    }
    return render(request, 'meetups/meetup-details.html', {
        "meetup_title": selected_meetup['title'],
        "meetup_description": selected_meetup['description']
    },)