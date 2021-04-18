from mainapplic.models import Submission
from rest_framework import  serializers, viewsets

# Serializers define the API representation.
class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ['title','date_of_creation']


# ViewSets define the view behavior.
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer