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