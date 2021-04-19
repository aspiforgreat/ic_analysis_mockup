from mainapplic.models import *
from rest_framework import  serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BenchmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Benchmark
        fields = ['score','accuracy']

class BenchmarkViewSet(viewsets.ModelViewSet):
    queryset = Benchmark.objects.all()
    serializer_class = BenchmarkSerializer


class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Algorithm
        fields = ['title','description']

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ['title']


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


# Serializers define the API representation.
class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        benchmark = BenchmarkSerializer(read_only=True)
        algorithm = AlgorithmSerializer(read_only=True)
        dataset = DatasetSerializer(read_only=True)
        user = UserSerializer(read_only=True)
        fields = ['title','date_of_creation','benchmark','algorithm','dataset','user']


# ViewSets define the view behavior.
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer