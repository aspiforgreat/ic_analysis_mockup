from django.db import models

class Algorithm (models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

class Benchmark(models.Model):
        score = models.FloatField()
        accuracy = models.FloatField()

        def __str__(self):
            return  str(self.score) + " and "+  str(self.accuracy)


class Dataset(models.Model):
    title = models.CharField(max_length=300)
    #leaderboardAccess = models.OneToOneField('Leaderboard', related_name='leaderboard',on_delete=models.DO_NOTHING,blank=True)
    data = models.ImageField(upload_to='images',default='static/assets/images/banner-bg.jpg')

    def __str__(self):
        return self.title


 #relate to an algorithm, a benchmark and a dataset but as a foreign key so we can resubmit the same algorithm with the same benchmark an dataset
    # one way relation so centralized control but on delete DoNothing so we can resubmit
class Submission(models.Model):
    title = models.CharField(max_length=300,default="Untitled Submission")
    date_of_creation = models.DateField()


    benchmark = models.ForeignKey('Benchmark', blank=False,on_delete=models.DO_NOTHING)
    algorithm = models.ForeignKey('Algorithm', blank=False,on_delete=models.DO_NOTHING)
    dataset =models.ForeignKey('Dataset', blank=False,on_delete=models.DO_NOTHING)

    user = models.ForeignKey('User', blank=False,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title



# One User has Many Submissions, A submission only has one User but Many Users have Many Submissions
    # so submission has a foreign key
class User(models.Model):
    name =  models.CharField(max_length=100)


    def __str__(self):
        return self.name


#a Leaderboad has a lot of lines but a leaderboard line is only related to one leaderboard
    # designed it this way makes us have to assign the rank to each leaderboardline and then update it manually,
    # might be better to compute it and display it, but might be a high effort every time
class Leaderboard(models.Model):
    dataset = models.OneToOneField(Dataset,on_delete=models.CASCADE,blank= False)

    def __str__(self):
         return self.dataset.__str__() + " Leaderboard"



class LeaderboardLine(models.Model):
    rank = models.IntegerField()
    leaderboard = models.ForeignKey(Leaderboard,blank=False,on_delete=models.CASCADE)

    # submission will provide the score, algorithm name and accuracy
    submission = models.OneToOneField(Submission,primary_key=True,on_delete=models.CASCADE,blank=False)


