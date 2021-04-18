from django.shortcuts import render
from .models import *
from django.http import Http404
# Create your views here.


def home(request):
    return render(request, 'index.html')

#here we can use the algorithmsSource to pass parameter that are then displayed in views
#call the compute function pass a dataset and get back a result
#passing a dataset here might be a bad idea better delegate to another class so here we only choose what to display

def leaderboard(request,leaderboard_id):
    try:
        leaderboard = Leaderboard.objects.get(id = leaderboard_id)
    except Leaderboard.DoesNotExist:
        raise Http404('Employee not found')
    #render the request in an html and pass the dictionary with the info we eed
    return render(request,'leaderboard.html',{'leaderboard':leaderboard})

def leaderboardList(request):
    leaderboards = Leaderboard.objects.all()
    return render(request,'leaderboardList.html',{'leaderboards':leaderboards})

def datasets(request):
        datasets = Dataset.objects.all()
        # render the request in an html and pass the dictionary with the info we eed
        return render(request, 'datasets.html', {'datasets': datasets})

