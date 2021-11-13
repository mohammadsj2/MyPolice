from django.db import models

# Create your models here.
class Mission(models.Model):
    location = models.CharField(max_length=1000)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return "|loc: " + self.location + "|start: " + str(self.start_time) + "|end: " + str(self.end_time) + "|desc: " + self.description + "|"

class Police(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    location = models.CharField(max_length=1000)
    status = models.CharField(max_length=200)
    current_mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='current_police')
    missions = models.ManyToManyField(Mission, through='MissionPolice', related_name='all_police')

class MissionPolice(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    police = models.ForeignKey(Police, on_delete=models.CASCADE)
    join_time = models.TimeField(auto_now=False, auto_now_add=False)
    leave_time = models.TimeField(auto_now=False, auto_now_add=False)
