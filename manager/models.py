from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Mission(models.Model):
    location = PlainLocationField(based_fields=['city'], zoom=7)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    description = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return "|loc: " + self.location + "|desc: " + self.description + "|"

class Police(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birthday = models.DateField(max_length=200, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    current_mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='current_police', blank=True, null=True)
    missions = models.ManyToManyField(Mission, through='MissionPolice', related_name='all_police')

    def __str__(self) -> str:
        return f'username: {self.username}, password: {self.password}, name: {self.name}'

class MissionPolice(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    police = models.ForeignKey(Police, on_delete=models.CASCADE)
    join_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    leave_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.mission) + " " + str(self.police) + " " + str(self.join_time)
