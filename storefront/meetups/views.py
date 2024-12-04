from django.shortcuts import render
# from django.http import HttpResponse

# the path is relative to the teamplates directory already
def index(request):
    return render(request, 'meetups/index.html')