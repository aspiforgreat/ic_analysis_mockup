from django.contrib import admin

from mainapplic.models import *


# Register your models here.


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['title','date_of_creation', 'user']

@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ['title','description']


@admin.register(Benchmark)
class BenchmarkAdmin(admin.ModelAdmin):
    list_display = ['score','accuracy']


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
  pass

@admin.register(LeaderboardLine)
class LeaderboardLineAdmin(admin.ModelAdmin):
    list_display = ['rank','submission','leaderboard']



