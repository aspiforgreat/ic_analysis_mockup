from django.shortcuts import render
from .models import *
from django.http import Http404


# Create your views here.
def home(request):
    return render(request, 'index.html')

#here we can use the algorithmsSource to pass parameter that are then displayed in views
#call the compute function pass a dataset and get back a result
#passing a dataset here might be a bad idea better delegate to another class so here we only choose what to display


# was in its own file, we should split this into its own controller for each class
#and leave views to be the main controller, this is pretty useless if u have a viewset but well
from rest_framework import status
from rest_framework.response import Response
from .models import Submission
from ic_analysis_mockup.serializers import SubmissionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def submissionList(request):
    """
    List all submissions, or create a new submission.
    """
    if request.method == 'GET':
        submissions = Submission.objects.all()
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)