from django.db import models

# Create your models here.
class Mission(models.Model):
    location = models.CharField(max_length=1000)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return "|loc: " + self.location + "|start: " + str(self.start_time) + "|end: " + str(self.end_time) + "|desc: " + self.description + "|"