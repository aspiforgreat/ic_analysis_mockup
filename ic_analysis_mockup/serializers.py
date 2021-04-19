from mainapplic.models import *
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


# Serializers define the API representation.
class BenchmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Benchmark
        fields = ['score','accuracy']

# ViewSets define the view behavior.
class BenchmarkViewSet(viewsets.ModelViewSet):
    queryset = Benchmark.objects.all()
    serializer_class = BenchmarkSerializer



class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Algorithm
        fields = ['title','description']

# ViewSets define the view behavior.
class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ['title']


# ViewSets define the view behavior.
class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer